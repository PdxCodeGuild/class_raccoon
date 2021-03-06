'''
Lab 21: Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
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


