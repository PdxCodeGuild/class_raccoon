from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

@app.route('/', methods=['GET', 'POST'])
def index():

    data = load_database()

    if request.method == 'POST':
        text = request.form['activity']
        priority = request.form['priority']

        data['todos'].append({'text':text, 'priority':priority})

    save_database(data)

    return render_template('index.html', data=data['todos'])
