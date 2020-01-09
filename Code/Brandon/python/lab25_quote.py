import requests
import random
import json

url = "https://favqs.com/api/qotd"



def random_quote():
    while True:
        response = requests.get(url)
        data = json.loads(response.text)
        print(data["quote"]["author"])
        print(data["quote"]["body"])
        again = input("Do you want to see another quote?")
        if again != "yes":
            break

def keyword():
    page = 1
    user = input("Which keyword would you like to search?\n:")
    while True:
        keyword_url = f'https://favqs.com/api/quotes?page={page}&filter={user}'
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(keyword_url, headers=headers)
        data = json.loads(response.text)
        quotes = (data["quotes"])
        for quote in quotes:
            print(f"Author: {quote['author']}\n{quote['body']}")
            print("")
        again = input("Do you want to see the next page?")
        if again == "yes":
            page += 1
        else:
            print("Goodbye....")
            


what_to_do = input("Chose from the following:\n (1)Display a random quote.\n (2)List quote by keywords.\n:")
if what_to_do == "1":
    random_quote()
elif what_to_do == "2":
    keyword()

    
    