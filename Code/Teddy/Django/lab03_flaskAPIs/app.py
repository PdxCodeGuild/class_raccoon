
from flask import Flask, render_template, redirect, request
import requests
import json

app = Flask(__name__)


def read_database():
    with open('database.json') as file:
        data = json.loads(file.read())
    return data

def write_database(data):
    data = json.dumps(data, indent=2)
    with open('database.json', 'w') as file:
        file.write(data)

@app.route('/')
def index():
    response = requests.get('https://favqs.com/api/qotd')
    data = json.loads(response.text)
    quote_author = data['quote']['author']
    quote_text = data['quote']['body']
    data = read_database()
    return render_template('index.html', quote_author=quote_author, quote_text=quote_text, data=data['quote'])


@app.route('/save/', methods=['POST'])
def save():
    quote_text = request.form['quote_text']
    quote_author = request.form['quote_author']

    quotes = {
        'body': quote_text,
        'author': quote_author
    }
    data = read_database()
    data['quote'].append(quotes)
    write_database(data)
    return redirect('/')

@app.route('/delete/', methods=['POST'])
def deletetodo():
    quote_index = int(request.form['quote_index'])
    data = read_database()
    data['quote'].pop(quote_index)
    write_database(data)
    return redirect('/')
