

from flask import Flask, render_template
import json

app = Flask(__name__)


def read_database():
    with open('database.json') as file:
        data = json.loads(file.read())
    return data

def write_database(data):
    data = json.dumps(data)
    with open('database.json', 'w') as file:
        file.write(data)

@app.route('/'. methods=['GET', 'POST'])
def index():
    data = read_database()
    if request.method == 'POST':
        text = request.form['text']
        priority = request.form['priority']
        todo = {
            'text': text,
            'priority': priority
        }
        data['todos'].append(todo)
        write_database(data)
    return render_template('index.html', todos=data['todos'])


