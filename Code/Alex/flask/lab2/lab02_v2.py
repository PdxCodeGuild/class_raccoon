

from flask import Flask, request, render_template
import json

app = Flask(__name__)



def load_database():
    with open('database.json','r') as file:
        data = json.loads(file.read()) # json string -> python dictionary
        data = data['todos']
    return data


def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))



@app.route('/', methods=['GET', 'POST'])
def index2():
    add_text = ''
    add_intensity = ''
    data = load_database()

    if request.method == 'POST':
        add_text = request.form['add_text']
        add_intensity = request.form['add_intensity']
        data.append({'text':add_text, 'intensity':add_intensity})
        save_database({"todos":data})
    return render_template('index2.html', data=data, add_text=add_text, add_intensity=add_intensity)

