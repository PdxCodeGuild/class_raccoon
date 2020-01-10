
'''
Lab 25 Quote API

For this lab we'll be using the Favqs Quotes API to first get a random quote,
and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests and json libraries.
The example below uses a Chuck Norris joke API.

import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url) # send the request to the api
print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary
print(data['value']) # get a part of the response data out of the dictionary

Version 2: List Quotes by Keyword

'''

import requests
import json

while True:
    print()
    # User input options is "keyword" or "quit"
    user_input = input('"keyword" or "quit": ').lower()
    # if user type 'quit'
    if user_input == 'quit':
        # display message
        print('Bye')
        # get out of the program
        break

    # if the user type 'keyword'
    elif user_input == 'keyword':
        # Input keyword
        keyword = input('What is the keyword: ').lower()
        # request URL
        url = f'https://favqs.com/api/quotes?page=1&filter={keyword}'
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers=headers)
        # look at the raw json
        # turn the json into a python dictionary
        data = json.loads(response.text)
        # print()
        # print(data)
        # print()
        # print(data['quotes'][0]['body'])
        # print()

        for i in data['quotes']:
            print(i['body'])
            print()
    else:
        print('Your input does not recognized')
