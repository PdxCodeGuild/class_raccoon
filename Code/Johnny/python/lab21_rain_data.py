import requests
import re
import math
import datetime


response = requests.get("https://or.water.usgs.gov/non-usgs/bes/albina.rain")
data = response.text
data = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)

days = []
for day in data:
    date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    days.append((date,day[1]))
print(days)
