#Rain lab Brandon G. 
from datetime import datetime
import re
import requests
import math


#Requests the data from the web
def get_rain_data():
    response = requests.get("https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain")
    response = response.text
    return(response)

#Separates the data, strips just the date and time and the rainfall for the day
def get_rain_info(rain_data):
    data = re.findall(r"(\d{2}-\w+-\d{4})\s+(\d+)",rain_data)
    days = []
    for day in data:
        date = datetime.strptime(day[0], '%d-%b-%Y' )
        days.append((date,day[1]))
    return days

#Converts data into a list of tuples and assigns it to a dictionary
def annual_rain(data):
    annual_rainfall = {}
    for day in data:
        if day[0].year in annual_rainfall:
            annual_rainfall[day[0].year] += int(day[1])
        else:
            annual_rainfall[day[0].year] = int(day[1])
    return annual_rainfall

#Allows user to see the annual rainfall for a specified year.
def year_rainfall(data):
    pick_year = input("What year do you want the rainfall totals for?\n:")
    pick_year = int(pick_year)
    if pick_year in data:
        return (f"The annual rainfaul of {pick_year} is {round(data[pick_year]*.01,2)} inches.")

#Displays the mean annual rainfall data only for Hayden Island
def mean_rainfall(data):
    mean_data = 0
    for day in data:
        mean_data += int(day[1])
    mean_data = round((mean_data / len(data)*.01),2)
    return mean_data
    # return(f"The mean annual rainfaul of Hayden Island from 1998-2019 is {mean_data} inches.")

#Displays the variance for the annual rainfall using the data from the dictionary.
def standard_deviation_rainfall(mean_data,data):
    variance_list = []
    for day in data:
        variance_list.append((int(day[1])*.01 - mean_data)**2)
    totals = sum(variance_list)
    variance = round(totals / (len(variance_list)-1),2)
    standard_deviation = round(math.sqrt(variance),3)
    return standard_deviation

def most_rainfall(data):
    high_year = annual_rain(data)
    counter = 0 
    year = ''
    highest_day = 0
    day = ''
    for key in high_year:
        if high_year[key] > counter:
            counter = high_year[key]
            year = key
    for value in data:
        if highest_day < int(value[1]):
            highest_day = int(value[1])
            day = value[0]

    return (f" the rainiest year was {year} and it rained {counter*.01} inches. The rainiest day was {day.strftime('%d-%b-%Y')} and it rained {highest_day*.01} inches.")
    
  


while True:
    data = get_rain_data()
    data = (get_rain_info(data))

    annual_rainfall = annual_rain(data)
    mean = mean_rainfall(data)
    
    action = input("What would you like to do? chose from the following -- \n(1) For annual rainfall for chosen year. \n(2) for the mean rainfall from 1998-2019. \n(3) for the standard deviation and \n(4) for the day that produced the most rain and the year that produced the most rain on average. \n(5) TO QUIT\n:")
    if action == "1":
        print(year_rainfall(annual_rainfall))
    elif action == "2":
        print(f"The mean rainfall for Hayden Island between 1998 and 2019 is {mean_rainfall(data)}")
    elif action == "3":
        print(f"The mean standard deviation for Hayden Island between 1998 and 2019 is {standard_deviation_rainfall(mean,data)}")
    elif action == "4":
        print(most_rainfall(data))
    elif action == "5":
        print("Goodbye")
        break










