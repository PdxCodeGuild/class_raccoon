#lab25_quote.py

import requests
import json

print("Random Quotes Generator!")

#Version 1 - Get a random quote
url = 'https://favqs.com/api/qotd' #Quote of the day
response = requests.get(url) # send the request to the api
# print(response.text) # look at the raw json
data = json.loads(response.text)['quote'] # turn the json into a python dictionary
print(f'"{data["body"]}"')
print(data['author'])

#Version 2 - List quotes by keyword
print("Now let's get a list of quotes!")
userinput = input("Enter a keyword to search for quotes: ")

nextpg = True
page = 0
counter = 0
while nextpg:
    page += 1
    url = f'https://favqs.com/api/quotes?page={page}&filter={userinput}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    data = json.loads(response.text)['quotes']

    if data[0]['id'] == 0: #this is the id for no quotes found
        if page == 1: #returns if no quotes found on page 1, does not return if no quotes found on additional pages (i.e. page 1 had quotes, but page 2 did not return any)
            print('No quotes found!')
        nextpg = False
        continue

    if page > 1: #prompt user to view additional pages after page 1
        asknext = ''
        while asknext != 'done' and asknext != 'next page':
            asknext = input("Enter 'next page' to continue or 'done' to quit: ")
            if asknext == 'done':
                nextpg = False

    if nextpg:
        # loops through quotes if the above functions did not kill the loop
        for key in data:
            counter += 1 #running tally of quote numbers
            print(f"Quote {counter}:")
            print(f'"{key["body"]}"')
            print(key['author'])