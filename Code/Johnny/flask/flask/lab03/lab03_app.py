from flask import Flask, render_template, redirect, request
from secrets import giphy_api
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_search = request.form['search']
        search = requests.get(f'https://api.giphy.com/v1/gifs/search?{giphy_api}&q={user_search}&limit=25&offset=0&rating=G&lang=en')
        search_output = data['data']['image_url']
    else:
        response = requests.get(f'https://api.giphy.com/v1/gifs/random?{giphy_api}&tag=&rating=G')
        data = json.loads(response.text) # loads response from website
        output = data['data']['image_url']
        print(data['data']['image_url']) # this is printing out what output is.
    return render_template('index.html', output=output)
