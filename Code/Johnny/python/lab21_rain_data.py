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


# Using lambda to figure out max value at end of tuples and return date
print('Day with most rainfall: ')
print(max(days_most, key = lambda i : i[1])) #shows full value and date
res = max(days_most, key = lambda i : i[1])[0] #shows date and time (inner tuples)
print(res)
# trying to calcuate the total means
# extract total from list and convert to int to calcuate
total_mean = [i[1] for i in days_most]
total_mean = [int(i) for i in total_mean]
print(len(total_mean)) #7196
print(sum(total_mean))
print(sum(total_mean)/7196)
