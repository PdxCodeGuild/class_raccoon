import requests
import datetime
import re
import math
import matplotlib.pyplot as plt

rain_data = []
#Pull in rain data file
#Turn it into a useable format
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/twelfth_and_clay.rain')
page_source = response.text

rain_data = re.findall(r"(\d{2}-\w{3}-\d{4})\s+(\d+)", page_source)

#Use datetime to make the dates useable
temp_list = []
for dates in rain_data:
    date = datetime.datetime.strptime(dates[0], "%d-%b-%Y")
    temp_list.append((date, int(dates[1])))
rain_data = temp_list
#Clean rain_data


temp_list = []
for rain in rain_data:
    if rain[1] != "":
        temp_list.append(rain)
rain_data = temp_list



def get_mean(rain_data):
    rain_totals = 0
    for rain in rain_data:
        rain_totals += (int(rain[1]))
    result = rain_totals/len(rain_data)     
    return result

rain_mean = get_mean(rain_data)
rainmean_inches = round(rain_mean * .01, 3)

def variance_is_stupid(rain_data, rain_mean):
    rain_var = 0
    for rain in rain_data:
        rain_var += ((int(rain[1])-rain_mean)**2)
        rain_var /= (len(rain_data)-1) 
    return rain_var
rain_variance = math.sqrt(variance_is_stupid(rain_data, rain_mean))

def wettest_day(rain_data):
    soggiest_day = None
    # print(rain_data)
    for i in range(len(rain_data)):
        if soggiest_day == None:
            soggiest_day = rain_data[i]
        if rain_data[i][1] > soggiest_day[1]:
            soggiest_day = rain_data[i]
        # print(soggiest_day)
    return(soggiest_day)

the_rainening = wettest_day(rain_data)


def wettest_year(rain_data):
    the_rainpocolypse = None
    year_rain = 0
    year_rain_comp = 0
    years = []
    for days in rain_data:
        if days[0].year not in years:
            years.append(days[0].year)
    for year in years:
        for day in rain_data:
            if day[0].year == year:
                year_rain += day[1]
        if year_rain > year_rain_comp:
            year_rain_comp = year_rain
            the_rainpocolypse = (day[0].year , year_rain_comp)
    return the_rainpocolypse

the_rainpocolypse = wettest_year(rain_data)

# def graphit(rain_data):
x_values = []
y_values = []
year = int(input("What year would you like to graph? (2001-2019) "))
for days in rain_data:
    if year == days[0].year:
        x_values.append(days[0])
        y_values.append(days[1])
plt.plot(x_values, y_values)
plt.show()



print(f"The mean is {rainmean_inches} and the variance is {round(rain_variance,3)}. The wettest day was {the_rainening[0].strftime('%d-%b-%Y')} with {the_rainening[1]} inches of rainfall. The wettest year, also known as the rainpocalypse was {the_rainpocolypse[0]} with {the_rainpocolypse[1]*.01} inches.")



