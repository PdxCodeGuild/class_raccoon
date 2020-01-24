from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)


def save_database(data):
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
    return data



@app.route('/')
def index():
    data = load_database()
    data = data['todos']
    return render_template('index.html',data=data)
    

@app.route('/post/',methods=["POST"])
def add():
    data = load_database()
    data = data['todos']
    priority = request.form["priority"]
    add = request.form["add"]
    data.append({"text":add, "priority":priority})
    save_database({"todos":data})
    return redirect('/')



    