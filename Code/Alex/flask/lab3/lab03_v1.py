from flask import Flask, render_template, request
import requests
import json
import secrets

app = Flask(__name__)


def load_database():
    with open('database.json','r') as file:
        data = json.loads(file.read()) # json string -> python dictionary
        data = data['location']
    return data


def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))



@app.route('/', methods= ['GET', 'POST'])
def index1():

    data = ''

    if request.method == "POST":

        location = request.form['location']
        url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&q={location}&APPID={secrets.api_key}'
        response = requests.get(url)
        data = json.loads(response.text)

    return render_template('index1.html', data=data)

