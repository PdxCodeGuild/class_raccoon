# lab25_quotes_api.py
import requests
import json

# start a loop to ask if they want another joke.
while True:
    url = 'https://favqs.com/api/qotd'
    response = requests.get(url) # send the request to the api
    # print(response.text) # look at the raw json
    # data = json.loads(response.text)['quote'] trying to access dictionary keyword 'quotes' in dictionary
    data = json.loads(response.text) # turn the json into a python dictionary

# get a part of the response data out of the dictionary


    print(data['quote']['body']) # accessing dict 'quotes', find 'body' and sends out quotes
    print('>>> ' + data['quote']['author'] + ' <<<') # key 'quotes', 2nd dict 'author', sends back author name
    
    # ask if they want another joke or not loop
    again = input('Do you want another joke? ').lower()
    if again != 'yes':
        break
