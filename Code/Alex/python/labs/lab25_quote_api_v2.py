'''
Lab 25 Quote API: Version 2

List Quotes by Keyword

The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:


This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

url = 'https://favqs.com/api/quotes?page=1&filter=nature'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
'''


import requests
import json
import os

def quotes(keyword, quote):
    url = 'https://favqs.com/api/qotd'
    response = requests.get(url)
    #print(response.text)
    data = json.loads(response.text)
    body = data['quote']['body']
    author = data['quote']['author']

    print(f"\"{body}\"\n-{author}")


keyword = input("enter a keyword to search for quotes: ").lower()
page = 1

while True:
    os.system("clear")
    
    new_url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    response = requests.get(new_url)
    #data = json.loads(response.text)
    print(f"{response}\n\n")

    page_or_quit = input("enter 'next page' or 'done': ").lower()
    if page_or_quit == "next page":
        page += 1
        if page_or_quit == 'done':
            break

