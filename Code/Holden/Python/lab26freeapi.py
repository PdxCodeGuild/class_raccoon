import json
import requests
import re
import time

def call_db(database, prin=0, headers=None):
    if headers:
        response = requests.get(database, headers=headers)
    else:
        response = requests.get(database)
    if prin == 1:
        print(response.text)
    return json.loads(response.text)
past_request = time.time()-2
blacklist = "?blacklistFlags=nsfw"
while True:
    usin = input("What type of joke do you want? (any, miscellaneous, programming, dark) (q to quit)").lower()
    if usin == "nsfw":
        print("nsfw jokes activated")
        blacklist = ""
        continue
    if usin == "sfw":
        print("sfw mode activated")
        blacklist = "?blacklistFlags=nsfw"
        continue
    if usin == "quit" or usin == "q":
        break
    if usin == "any":
        choice = "Any"
    elif usin == "miscellaneous" or usin == "misc":
        choice = "Miscellaneous"
    elif usin == "programming":
        choice = "Programming"
    elif usin == "dark":
        choice = "Dark"
    else:
        print("please choose a valid category.")
        continue
    database = f"https://sv443.net/jokeapi/category/{choice}{blacklist}"
    current = time.time()
    if past_request + 2 > current:
        time.sleep(past_request + 2 - current)
    joke = call_db(database)
    past_request = time.time()
    if joke["type"] == "single":
        input(joke["joke"])
    if joke["type"] == "twopart":
        input(joke["setup"])
        input(joke["delivery"])
