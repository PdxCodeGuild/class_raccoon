'''*not complete*
Lab 21: Rain data

Version 2

Now that you've successfully extracted the data, let's done some statistics.

1. Calculate the mean of the data:

mean

2. Use the mean to calculate the standard deviation, which is a measure of how "spread out" the data is:

standard_deviation

68.2% of the data falls within 1 standard deviation of the mean.

bell_curve

3. Find the day which had the most rain.

4. Find the year which had the most rain on average.
'''


import re
import datetime

#write function to load the file
with open('rain_data.txt', 'r') as file:
    rain_data = file.read()
#create a list of tuples to represent the Data
data = re.findall("(\d{2}-\w{3}-\d{4})\s+(\d+)", rain_data)
#print(data)

#parse the dates with datetime.strptime. The result will be a datetime object
rain_data = []
for item in data:
    date = datetime.datetime.strptime(item[0], '%d-%b-%Y')
    rain_data.append((date, item[1]))
    #print(rain_data)
for item in rain_data[:100]:
    print(item[0].strftime('%d-%b-%Y'), item[1])





#calculate the mean of the DATA

#Use the mean to calculate the standard deviation

#Find the day which had the most rain.

#Find the year which had the most rain on average.