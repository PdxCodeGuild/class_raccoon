from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def add_task(todo_list, new_task, priority):
    todo_list.append({"text":new_task,"priority":priority})
    save_database({'todos':todo_list})
    return todo_list

def sort_list(todo_list):
    for todo in todo_list:
        if todo['priority'] == 'high':
            todo['num'] = 1
        elif todo['priority'] == 'medium':
            todo['num'] = 2
        else:
            todo['num'] = 3
    todo_list = sorted(todo_list, key = lambda i: (i['num']))
    return todo_list

@app.route('/', methods=['GET','POST'])
def index():
    todo_list = load_database()
    todo_list = todo_list['todos']
    todo_list = sort_list(todo_list)
    new_task = ''
    priority = ''

    if request.method == 'POST':
        if 'new_task' in request.form:
            new_task = request.form['new_task']
        if 'priority' in request.form:
            priority = request.form['priority']
        if new_task and priority:
            todo_list = add_task(todo_list, new_task, priority)
            todo_list = sort_list(todo_list)
    return render_template('index.html', new_task = new_task, priority = priority, todo_list = todo_list)