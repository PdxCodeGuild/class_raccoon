from flask import Flask, render_template, request
import json


# to run, type export 'FLASK_APP=app.py' or replace app with local file.
# then type 'flask run' or 'python -m flask run'
# to set flask in development type 'export FLASK_ENV=development'
app = Flask(__name__)

def load_database(): # reads json file
    with open("database.json", 'r') as file:
        data = json.loads(file.read())
        return data

@app.route('/')
def index():
    data = load_database() #loads json file as data
    return render_template('index.html', data=data)
