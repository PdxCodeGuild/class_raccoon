'''
Lab 26: Any API

Now build an interface around any API of your choosing. You can find a list of free public APIS here. Below are some recommendations.

Look at the documentation, find out the endpoints and general capabilities
Find a url and if possible, enter it into your browser and see if you can get JSON
Look into authentication, might have to register an account to get an API key
Send the request through Python, look at the format of the response
Copy the data into a JSON viewer
Write code to extract the relevant data and display it
OpenWeatherMap - data on weather
Trefle - data on plants
TheCatAPI - data about cats
PokeAPI - data about pokemon
Brickset API - data about legos responds with XML
'''


import webbrowser
import requests
import os
import random

while True:
    os.system("clear")
    user_choice = input("Type \"random\" to display a random gif, \"search\" to search for gifs or \"quit\" to quit. ").lower()
#random
    if user_choice == "random":
        os.system("clear")
        headers = {"api_key" : "rHH2bcJvdAtFJag6LLxFcAnHHZsfHBOm"}
        url = 'http://api.giphy.com/v1/gifs/random'
        response = requests.get(url, params=headers)
        data = response.json()
        gif = data["data"]["url"]
        webbrowser.open_new_tab(gif)
        print()
        print()
        random_again = input("Display another random gif? ").lower()
        while random_again == "yes" or random_again == "y":
            os.system("clear")
            url = 'http://api.giphy.com/v1/gifs/random'
            response = requests.get(url, params=headers)
            data = response.json()
            gif = data["data"]["url"]
            webbrowser.open_new_tab(gif)
            print()
            print()
            random_again = input("Display another random gif? ").lower()
        else:
            continue
#search
    elif user_choice == "search":
        term = input("What kind of gif are you looking for? ")
        headers = {"api_key" : "rHH2bcJvdAtFJag6LLxFcAnHHZsfHBOm", "q" : term}
        url = f'http://api.giphy.com/v1/gifs/search'
        response = requests.get(url, params=headers)
        data = response.json()
        search_again = "y"
        while search_again == "yes" or search_again == "y":
            os.system("clear")
            gifs = data["data"]
            gif = random.choice(gifs)
            webbrowser.open_new_tab(gif["url"])
            print()
            print()
            search_again = input("Search for another gif? ").lower()
            continue
        else:
            continue
#quit
    elif user_choice == "quit":
        break
#else
    else:
        input("invalid entry")
