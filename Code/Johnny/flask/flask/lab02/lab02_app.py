from flask import Flask, render_template, request
import json


# to run, type 'export FLASK_APP=app.py' or replace app with local file.
# then type 'flask run' or 'python -m flask run'
# to set flask in development type 'export FLASK_ENV=development'
app = Flask(__name__)

def load_database(): # reads json file
    with open("database.json", 'r') as file:
        data = json.loads(file.read())
        return data

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

@app.route('/', methods=['GET', 'POST'])
def index():
    data = load_database()  # load json database to parse straight to template
    if request.method == 'POST':
        add_text = request.form['text'] # assign var to form input 'text'
        add_priority = request.form['priority'] # assign var to input of 'priority'
        load_database()
        data['todos'].append({'text':add_text, 'priority':add_priority}) #append the dict['todos'] with inputs
        save_database(data)
    return render_template('index.html', data=data)
