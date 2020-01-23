

from flask import Flask, request, render_template
import json

app = Flask(__name__)



@app.route('/')
def index1():
    with open('database.json','r') as file:
        data = json.loads(file.read()) # json string -> python dictionary
        data = data['todos']
        return render_template('index1.html', data=data)


