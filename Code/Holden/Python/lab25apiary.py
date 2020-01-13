import json
import requests
import re

def call_db(database, prin=0, headers=None):
    if headers:
        response = requests.get(database, headers=headers)
    else:
        response = requests.get(database)
    if prin == 1:
        print(response.text)
    return json.loads(response.text)

def search_call(search_term, page = 1):
    url = f'https://favqs.com/api/quotes?page={page}&filter={search_term}'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = call_db(url, 0, headers)
    for i in range(len(response["quotes"])):
        print(f'"{response["quotes"][i]["body"]}" - {response["quotes"][i]["author"]}')
    return response["last_page"]

qotd = call_db(r"https://favqs.com/api/qotd")
print(f'Quote of the Day: \n"{qotd["quote"]["body"]}" - {qotd["quote"]["author"]}')

usin = input("enter a keyword to search for quotes: ").lower()
page = 1
last_page = search_call(usin, page)
while last_page == False:
    uscont = input('for next page type "next page", otherwise type "done": ').lower()
    if uscont == "next" or uscont == "next page":
        last_page = search_call(usin, page)
    else:
        break
