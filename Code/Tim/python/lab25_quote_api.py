import requests
import json
import random

url = 'https://favqs.com/api/qotd'
response = requests.get(url)
# print(response.text)
data = json.loads(response.text)
quote = data['quote']["body"]
author = data['quote']['author']
# print(quote + f' -{author}' )

# quote_dict = {}
#
# #building a dictionary of quotes and authors
# def building_dict(quote_dict):
#     for i in range(20):
#         response = requests.get(url)
#         # print(response.text)
#         data = json.loads(response.text)
#         quote = data['quote']["body"]
#         author = data['quote']['author']
#         quote_dict[author] = quote
#     return quote_dict
# quote_dict = building_dict(quote_dict)
#
# print(quote_dict)
tags = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'
get_tags = requests.get(tags)
get_tags = json.loads(get_tags.text)
print(get_tags)
