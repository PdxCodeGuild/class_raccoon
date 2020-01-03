


import requests
import re
import datetime

def get_rain_files():

    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    page_source = response.text
    rain_files = re.findall(r'\w+\.rain', page_source)
    # rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    return rain_files

def get_rain_file(file_name):
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/' + file_name)
    data = response.text
    data = re.findall(r'(\d{2}-\w{3}-\d{4})\s+(\d+)', data)
    data = [(datetime.datetime.strptime(row[0], '%d-%b-%Y'), float(row[1])*0.01*2.54) for row in data]
    data.sort(key=lambda x: x[0])
    return data



# rain_files = get_rain_files()
# rain_files.sort()
# for i in range(len(rain_files)):
#     print('\t', i, rain_files[i])
# file_index = int(input('what file would you like to look at? '))
# data = get_rain_file(rain_files[file_index])


data = get_rain_file('sunnyside.rain')

total = 0
for i in range(len(data)):
    total += data[i][1]
average = total / len(data)
print(average)


max_rain = max(data, key=lambda x: x[1])

print(max_rain)




years = [row[0].year for row in data]
years = list(set(years))
years.sort()
print(years)

year_counts = [0]*len(years)
year_totals = [0]*len(years)
for row in data:
    year_index = years.index(row[0].year)
    year_totals[year_index] += row[1]
    year_counts[year_index] += 1

year_averages = [year_totals[i]/year_counts[i] for i in range(len(years))]
for i in range(len(years)):
    print(years[i], year_averages[i], 'cm')
