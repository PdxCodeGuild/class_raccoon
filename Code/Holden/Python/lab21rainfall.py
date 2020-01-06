import requests
import re
import datetime
import math
from collections import OrderedDict

def get_rain_urls(database):
    print("grabbing list of files from database")
    response = requests.get(database)
    print("response received")
    page_source = response.text
    rain_file_names = re.findall(r'\w+\.rain', page_source)
    rain_files = [database + rain_file for rain_file in rain_file_names]
    url_tup=[]
    for i in range(len(rain_file_names)):
        url_tup.append((rain_files[i],rain_file_names[i]))
    return url_tup

database = 'https://or.water.usgs.gov/non-usgs/bes/'
url_list = get_rain_urls(database)
#url_list = [('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain','hayden_island.rain')]

def find_cache(url):
    try:
        content = open(f'RainData\\{url[1]}', 'r').read()
        print(f"{url[1]} content loaded from cache.")
    except FileNotFoundError:
        print("Trying to load website.")
        response = requests.get(url[0])
        content = response.text
        print(f'{url[1]} content loaded from website.')
        open(f'RainData\\{url[1]}', 'w').write(content)
    return content

def rain_data_totals(url):
    data_in = find_cache(url)
    day_tots = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data_in)
    output = []
    for day in day_tots:
        date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
        output.append((date, int(day[1])))
    return output

def full_rain(url):
    data_in = find_cache(url)
    day_tots = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)\s+(.+)', data_in)
    output = []
    for day in day_tots:
        date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
        output.append((date, day[1], day[2]))
    return output

def get_mean(data_list):
    mean = sum(data_list) / len(data_list)
    return mean

def std_dev(data_list):
    mean = get_mean(data_list)
    for i in range(len(data_list)):
        data_list[i] = (data_list[i] - mean)**2
    output = math.sqrt(get_mean(data_list)/(len(data_list)-1))
    return output

def sortSecond(val):
    return val[1]

for url in url_list:
    station_data = rain_data_totals(url)
    station_data.sort(key = sortSecond, reverse = True)
    print(f'Data from{url[1]}')
    print(f'Highest ever rain was on {station_data[0][0].strftime("%d-%b-%Y")} at {station_data[0][1]} tips, or {station_data[0][1]/100} inches.')
    dateless = []
    yearly = {}
    for datum in station_data:
        dateless.append(int(datum[1]))
        if datum[0].year not in yearly:
            yearly[datum[0].year] = [datum[1]]
        else:
            yearly[datum[0].year].append(datum[1])
    year_totals = []
    for year in yearly:
        year_data = []
        for datum in yearly[year]:
            year_data.append(datum)
        year_tot = sum(year_data)
        year_totals.append((year, year_tot))
    year_totals.sort(key= sortSecond, reverse = True)
    print(f'The average rainfall  was {get_mean(dateless)} with a standard deviation of {std_dev(dateless)}.')
    print(f"{year_totals[0][0]} had the most rainfall at {year_totals[0][1]/100} inches.")
