from flask import Flask, render_template, request, redirect
import random
import string
import urllib
import json

app = Flask(__name__)

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def number_tasks(data):
    i = 1
    for task in data:
        task["number"] = i
        i += 1
    return data

def add_to_list(data, new_task, priority_level):
    if new_task is not "":
        data.append({"text":new_task,"priority":priority_level})
        data = number_tasks(data)
    return data

@app.route('/', methods=['GET','POST'])
def index(): 
    file = load_database()
    data = file['todos']
    data = number_tasks(data)
    
    
    response = ""
    new_task = ""
    priority_level = ""
    if request.method == 'POST':
        # cypher = request.form['cypher']
        new_task = request.form['new_task']
        priority_level = request.form['priority_level']
        data = add_to_list(data, new_task, priority_level)
        file = {'todos':data}
        save_database(file)
        response = True
        new_task = ""
        priority_level = ""
        return render_template('lab02.html', data=data, new_task=new_task, response=response, priority_level=priority_level)
    return render_template('lab02.html', data=data, new_task=new_task, response=response, priority_level=priority_level)

@app.route('/delete/', methods=['POST'])
def delete():
    del_num = request.form['del_num']
    file = load_database()
    data = file['todos']
    temp_data = []
    for task in data:
        if task['number'] == del_num:
            break
        else:
            temp_data.append(task)
    data = number_tasks(temp_data)
    file = {'todos':data}
    save_database(file)

    return redirect('/')