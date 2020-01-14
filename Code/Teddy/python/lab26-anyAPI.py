'''
Lab 26: Any API

Now build an interface around any API of your choosing.
You can find a list of free public APIS here. Below are some recommendations.

    1. Look at the documentation, find out the endpoints and general capabilities
    2. Find a url and if possible, enter it into your browser and see if you can get JSON
    3. Look into authentication, might have to register an account to get an API key
    4. Send the request through Python, look at the format of the response
    5. Copy the data into a JSON viewer
    6. Write code to extract the relevant data and display it

OpenWeatherMap - data on weather
Trefle - data on plants
TheCatAPI - data about cats
PokeAPI - data about pokemon
Brickset API - data about legos responds with XML
'''
import requests
import re
import json
import datetime

url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2011-01-01&end=2020-01-08'
# Send the request through Python,
# assign all info in variable name response
response = requests.get(url)
# Put in Json file
data = json.loads(response.text)
data = data['bpi']
# assign the first colum in row to strings, and the second colum in row to float numbers in data
data = [(datetime.datetime.strptime(date_string, '%Y-%m-%d'), float(data[date_string])) for date_string in data]
data.sort(key=lambda x: x[0])
# print(data)

# for key in range(len(data)):
#     # print(f'Year: {key}, BTC Price-> ${data[key]}')
#     print(f'Year:{data[key][0]}, BTC price: ${data[key][1]}')



# Group the same year together
# Get only year from the first column of data
years = [row[0].year for row in data]

price = [row[1] for row in data]
# Then group the same year together and them in the list
years = list(set(years))
# sort years
years.sort()

print()
print(f'{years}')
# print(price)


#
#
# # loop over the years
# i = 0
# for i in years:
#     # build a list of all the tuples for the given year
#     price = [data[i]]
#     i += 1
#     print(f'{price}')



# loop over the years
#     build a list of all the tuples for the given year
#     find the tuple with the maximum value within that list
#     print it out?


#
# total = 0
# # sum all the data of the second column(total rain)
# for i in range(len(data)):
#     max = max.(data[i][1])




for row in data:
    years = row[0].year
    for col in data:
        prices = row[1]

    print(years, prices)


# each_year_max = data[years]
# print(each_year_max)



# # # loop over the years
# for year in range(len(data)):
#     price = []
#     price = [data[year]]
#     # build a list of all the tuples for the given year
#
#     print(f' {price}')







# year_list = [row[1] for row in data]
# print(f'{year} {year_list}')
# print(year_list)



# Finding maximum price of each year
# for price in years:
#     max_price = max(years[price][1])
#
#     print(max_price)




#
# # Find the day which had the most rain.
# total = 0
# # sum all the data of the second column(total rain)
# for i in range(len(data)):
#     total += data[i][1]
# # average rain
# average = total / len(data)
# print(average)
#
#






# year_counts = [0]*len(years)
# year_totals = [0]*len(years)
#
# for row in data:
#     year_index = years.index(row[0].year)
#     year_counts[year_index] += 1
#     print(year_counts)

# print()
# print('The maximum BTC price of each year')
# print()

# # Group the same year together
# # Get only year from the first column of data
# years = [row[0].year for row in data]
# # Then group the same year together
# years = list(set(years))
# # sort them
# years.sort()
# print(years)
