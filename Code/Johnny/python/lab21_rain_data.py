import requests
import re
import datetime


response = requests.get("https://or.water.usgs.gov/non-usgs/bes/albina.rain")
data = response.text
data = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)
#print(data)
# ^^ above data shows list of dates inf format and total str [(15-APR-2000, '23')]

days_most = []
years_most = []
for day in data:
    dates = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    days_most.append((dates,day[1]))
    years_most.append(dates.year)
print(days_most)
