'''
Lab 21: Rain Data
Version 2
Now that you've successfully extracted the data, let's done some statistics.

Calculate the mean of the data:

mean

Use the mean to calculate the variance:

variance

Find the day which had the most rain.

Find the year which had the most rain on average.

'''
# Import libraries
import requests
import re
import datetime

# get all data from url https://or.water.usgs.gov/non-usgs/bes/
def get_rain_files():
    # request info from https://or.water.usgs.gov/non-usgs/bes/
    # assign all info in variable name response
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    # get file as a text and assign all info in variable name page_source
    page_source = response.text
    # find all data that contain letter filename.rain from page_source
    rain_files = re.findall(r'\w+\.rain', page_source)
    # return value
    return rain_files


def get_rain_file(file_name):
    # request info from https://or.water.usgs.gov/non-usgs/bes/ + file_name
    # assign all info in variable name response
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/' + file_name)
    # Put in text and assign all info in variable name data
    data = response.text
    # find all data that contain first 2 number then - then 3 letters then then 4 numbers from data
    data = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)
    # assign the first colum in row to strings, and the second colum in row to float numbers in data
    data = [(datetime.datetime.strptime(row[0], '%d-%b-%Y'), float(row[1])*0.01*2.54) for row in data]
    # sort by the first column(year)
    data.sort(key=lambda x: x[0])
    # return value
    return data

data = get_rain_file('sunnyside.rain')
print(data)

# Find the day which had the most rain.
total = 0
# sum all the data of the second column(total rain)
for i in range(len(data)):
    total += data[i][1]
# average rain
average = total / len(data)
print(average)

#get the maximum number(maximum total rain average)
max_rain = max(data, key=lambda x: x[1])
print(max_rain)

# Group the same year together
# Get only year from the first column of data
years = [row[0].year for row in data]
# Then group the same year together and put in the list, and assigned to variable name yeards
years = list(set(years))
# sort them
years.sort()
print(years)

# Find the year which had the most rain on average.
# innitailise variables
year_counts = [0]*len(years)
year_totals = [0]*len(years)

for row in data:
    # get year from by take the first index from years
    year_index = years.index(row[0].year)
    # get total rain in a same year
    year_totals[year_index] += row[1]
    # count in the same year
    year_counts[year_index] += 1

# find the average rain of each year
year_averages = [year_totals[i]/year_counts[i] for i in range(len(years))]
# print output of each year by loop though years
for i in range(len(years)):
    print(years[i], year_averages[i], 'cm')

# Find the year which had the most rain on average.
max_rain_year = max(year_averages)
for i in range(len(years)):
    if year_averages[i] == max_rain_year:
        print(f'The year of {years[i]} had the maximum rain')

print(max_rain_year)
