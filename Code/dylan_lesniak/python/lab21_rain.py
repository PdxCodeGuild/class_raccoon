'''
Filename: lab21_rain.py
Author: Dylan 
Purpose: Use requests and regex to gather online rain data
'''

#mods
import requests
import re
import datetime
import math
import matplotlib.pyplot as plt
import helper 
from inspect import currentframe, getframeinfo
import numpy as np


def get_rain_urls(): #gets every file with rain data
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    page_source = response.text
    rain_files = re.findall(r'\w+\.rain',page_source)
    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    return rain_files

def get_file_data(file):
    file_text = file.text
    file_text = file_text.split('\n')
    data_lines = [line.split(" ") for line in file_text[11:]] #the last value in the list is always an empty list, which breaks the program
    for i in range(len(data_lines)): #a lot of values wound up being ["","",""] so this cuts those.
        data_lines[i] = [char for char in data_lines[i] if char != ""]
    data_lines = [line[:2] for line in data_lines]
    data_lines = data_lines[:-1] 
    get_page_info(data_lines)

#our central hub. Defines most of the data by referencing other methods. 
def get_page_info(data_lines): 
    
    data_dicts = get_data_dicts(data_lines)
    data_avg = get_mean(data_dicts)
    data_var = get_variance(data_dicts,data_avg)
    data_std = math.sqrt(data_var)

    day_max = get_day_max(data_dicts)
    year_avg = get_year_avg(data_dicts)
    year_max = max(year_avg,key=year_avg.get)

    print(f"The average rainfall per day is {round(data_avg,2)} inches.")
    print(f"The variance on the data is {round(data_var,2)} inches with a standard deviation of {round(data_std,2)} inches.")
    print(f"The day with the most rain was {day_max[0]} with a total of {day_max[1]} inches.")
    print(f"The year with the most rain was {year_max}.")
    
    print("\nWould you like a graph of all the data (total), monthly average (month), or yearly rainfall(year)? ")
    graph_type = helper.text_checker(input("> "),["total","month","year"])
    if graph_type == "total":
        days_dict = get_days_dict(data_dicts)
        show_graph(days_dict)
    elif graph_type == "month":
        month_dict = get_month_dict(data_dicts)
        show_graph(month_dict)
    elif graph_type == "year":
        year_dict = get_year_dict(data_dicts)
        show_graph(year_dict, "yes") #this reverses the order, so it goes, farthest back to most recent
    else:
        print("ERROR: You should not have gotten here.")
        frameinfo = getframeinfo(currentframe())
        print ("line: ",frameinfo.lineno,"exit.")
    return 


def get_data_dicts(data_lines): 
    data_dicts = []
    for line in data_lines:
        date = datetime.datetime.strptime(line[0], '%d-%b-%Y') #formats the dates into a more workeable format
        if line[1] == "-":
            continue
        else:
            daily_total = int(line[1]) / 100 #converts tips into inches
        temp_dict = {"Date":date,"Daily Total": daily_total}
        data_dicts.append(temp_dict)
    return data_dicts

def get_mean(data_dicts):
    length = len(data_dicts)
    total = 0 
    for dictionary in data_dicts:
        total += dictionary["Daily Total"]
    average = total / length 
    return average

#each val - avg then squared. 
def get_variance(data_dicts,data_avg):
    squared_totals = []
    for dictionary in data_dicts:
        daily_total = dictionary["Daily Total"]
        daily_total -= data_avg
        daily_total *= daily_total
        squared_totals.append(daily_total)
    sum_of_totals = sum(squared_totals)
    variance = sum_of_totals / len(data_dicts)
    return variance
    
def get_day_max(data_dicts):
    daymax = max(data_dicts, key=lambda x:x['Daily Total'])       #baymax, lol 
    daymax = daymax["Date"].strftime('%d-%b-%Y'), daymax["Daily Total"]
    return daymax



#make a dict of dicts. Year and then two values for total and days. 
#for each year, you take the total rainfall and divide it by the number of days
def get_year_avg(data_dicts):
    year_values = {}
    for dictionary in data_dicts:
        date = dictionary["Date"]
        year = date.year
        rain = dictionary["Daily Total"]
        if year in year_values:
            year_values[year]["total"] += rain
            year_values[year]["days"] += 1
        else:
            year_values[year] = {"total":rain,"days":1}
    year_avgs = {}
    for year in year_values:
        year_avgs[year] = (year_values[year]["total"] / year_values[year]["days"])
    return year_avgs

def get_days_dict(data_dicts):
    days_dict = {}
    for day in data_dicts:
        date = day["Date"].strftime('%d-%b-%Y')
        daily_total = day["Daily Total"]
        days_dict[date] = daily_total
    return days_dict

def get_month_dict(data_dicts):
    months_dict = {}
    for day in data_dicts:
        month = day["Date"].month
        daily_total = day["Daily Total"]
        if month in months_dict:
            if "rain" in months_dict[month]:
                months_dict[month]["rain"] += daily_total
                months_dict[month]["days"] += 1
            else:
                months_dict[month]["rain"] = daily_total
                months_dict[month]["days"] = 1
        else:
            months_dict[month] = {"rain": daily_total, "days": 1}
    months_avg = {}
    months_list = [month for month in months_dict]
    months_list.sort()
    for month in months_list: #gives us the month back in a readable string. For output in the graph later. 
        months_avg[datetime.date(1900,month,1).strftime('%B')] = round(months_dict[month]["rain"] / months_dict[month]["days"], 2)
    return months_avg

def get_year_dict(data_dicts):
    year_dict = {}
    for day in data_dicts:
        year = day["Date"].year
        daily_total = day["Daily Total"]
        if year in year_dict:
            year_dict[year] += daily_total
        else:
            year_dict[year] = daily_total
    for year in year_dict:
        year_dict[year] = round(year_dict[year],2)
    return year_dict
    

#puts the data into a proper format to be displayed in a graph
def get_xy_values(graph_dictionary,reverse = "no"):
    x_values = []
    y_values = []
    if reverse == "yes":
        for year in graph_dictionary:
            x_values.insert(0,year)
            y_values.insert(0,round(graph_dictionary[year],2))
        xy_values = [x_values,y_values]
    else:
        for year in graph_dictionary:
            x_values.append(year)
            y_values.append(round(graph_dictionary[year],2))
        xy_values = [x_values,y_values]
    return xy_values  

def show_graph(dict_to_show, reverse = "no"): 
    xy = get_xy_values(dict_to_show, reverse)
    month = np.array(xy[0])
    y = xy[1]
    plt.xticks(range(len(y)), month)
    plt.plot(y)
    plt.show()


if __name__ == "__main__":
    rains = get_rain_urls()
    files = []
    for rain in rains:
        files.append(requests.get(rain))
    file_list = []
    for file in files:
        for line in file:
            file_list.append(line)
    get_file_data(file_list) #make file_list a filetype (or whatever), not a list 
    

#data starts at array value 11. This is consistent on the forms, thankfully. 
