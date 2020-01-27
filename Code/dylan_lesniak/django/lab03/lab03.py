import secrets
from flask import Flask, render_template, request, redirect
import requests
import random
import string
import urllib
import json

app = Flask(__name__)


#v1 - Display data. Starting with v. 2 since once that's done the text / pictures will be easier. 
#v2 - user can choose where the weather data is coming from
#v3 - create a 'database' of the user's favorite places to search. 
#start with just the information. Then see if you can integrate the map. Which might be tough as it's based on coordinates, it seems. 

@app.route('/', methods=['GET','POST'])
def index(): 
    key = secrets.key 
    countries_dict = load_database('country_code.json')
    country = ""
    zip_code = ""
    response = "" 
    temp = ""
    min_temp = ""
    max_temp = ""
    description = ""
    if request.method == 'POST':
        response = True
        country = request.form["country"]
        zip_code = request.form["zip_code"]
        weather = get_weather(country, zip_code, key)
        print (weather)
        temp = weather['main']['temp']
        temp = (temp - 273.15) * 9/5 + 32
        min_temp = weather['main']['temp_min']
        min_temp = (min_temp - 273.15) * 9/5 + 32
        max_temp = weather['main']['temp_max']
        max_temp = (max_temp - 273.15) * 9/5 + 32
        description = weather['weather'][0]['description']
        lon = weather['coord']['lon']
        lat = weather['coord']['lat']
    return render_template('index.html', key=key, response=response, countries_dict=countries_dict, country=country, zip_code=zip_code, temp=temp, min_temp=min_temp,max_temp=max_temp,description=description)

def load_database(filename):
    with open(filename, 'r') as file:
        data = json.loads(file.read())
    return data

def get_weather(country, zip_code, key):
    query = '&APPID='
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip_code + ',' + country + query + key
    print(url   )
    response = requests.get(url)
    weather = json.loads(response.text)
    return weather