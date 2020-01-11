'''
Lab 21 Rain Data: Version 3

Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib. You can learn more about matplotlib here.

import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
Some charts you can make are:

all the data, date vs daily total
monthly totals, average across multiple years
total yearly rainfall, year by year
'''


import re
import datetime
import math
import matplotlib.pyplot as plt


with open('rain_data.txt', 'r') as file:
    rain_data = file.read()

data = re.findall("(\d{2}-\w{3}-\d{4})\s+(\d+)", rain_data)
rain_data = []
for item in data:
    date = datetime.datetime.strptime(item[0], '%d-%b-%Y')
    rain_data.append((date, item[1]))


#calculate the mean of the DATA
count_for_the_total = 0
for i in range(len(rain_data)):
    count_for_the_total += int(rain_data[i][1])
total = count_for_the_total
mean = total / len(rain_data)
print(f"\n\nThe mean of the data is {mean}\n")

#Use the mean to calculate the standard deviation
standard_deviation = []
for i in range(len(rain_data)):
    standard_deviation.append((int(rain_data[i][1]) - mean)**2)
s_mean = sum(standard_deviation) / len(standard_deviation)
s_mean = math.sqrt(s_mean)
print(f"The standard deviation of the data is {s_mean}\n")

#Find the day which had the most rain.
day_most_rain = rain_data[0]
for item in rain_data:
    if item[1] > day_most_rain[1]:
        day_most_rain = item
print(f"The day with the most rain had {day_most_rain[1]} tips\n")

#Find the year which had the most rain on average.
year_dict = {}
for day in rain_data:
    if day[0].year in year_dict:
        year_dict[day[0].year] += int(day[1])
    else:
        year_dict[day[0].year] = int(day[1])

year_most_rain = None
for item in year_dict:
    if year_most_rain == None:
        year_most_rain = (item, year_dict[item])
    elif year_dict[item] > year_most_rain[1]:
        year_most_rain = (item, year_dict[item])
print(f"The year with the most rain was {year_most_rain[0]} with a total rainfall of {year_most_rain[1]} tips.\n")

#Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals.
x_values = []
y_values = []
chosen_year = int(input("Pick a year (2001-2019) "))
for days in rain_data:
    if chosen_year == days[0].year:
        x_values.append(days[0])
        y_values.append(days[1])
plt.plot(x_values, y_values)
plt.ylabel(f"{chosen_year}'s rainfall")
plt.show()

