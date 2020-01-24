from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)




@app.route('/')
def todo():
    todo_list = []
    with open(r"lab02\database.json", "r") as file:
        data = json.loads(file.read())
    for item in data["todos"]:
        todo_list.append(item)
    return render_template('lab02todo.html', todo_list=todo_list)

@app.route('/save/', methods=['POST'])
def database_save():
    todo_list = []
    with open(r"lab02\database.json", "r+") as file:
        data = json.loads(file.read())
        new_todo = request.form["new_todo"]
        new_priority = request.form['new_priority']
        not_in_list = True
        high_p = []
        med_p = []
        lo_p = []
        no_p =[]
        for item in data["todos"]:
            if item["text"] not in request.form:
                if item['priority'] == 'high':
                    high_p.append(item)
                if item['priority'] == 'medium':
                    med_p.append(item)
                if item['priority'] == 'low':
                    lo_p.append(item)
                if item['priority'] == '':
                    no_p.append(item)
            if item["text"] == new_todo:
                not_in_list = False
        if not_in_list and new_todo:
            if new_priority == 'high':
                high_p.append({'text': new_todo, 'priority': new_priority})
            if new_priority == 'medium':
                med_p.append({'text': new_todo, 'priority': new_priority})
            if new_priority == 'low':
                lo_p.append({'text': new_todo, 'priority': new_priority})
            if new_priority == '':
                no_p.append({'text': new_todo, 'priority': new_priority})
        dataout = {"todos": high_p + med_p + lo_p + no_p}
        file.seek(0)
        file.write(json.dumps(dataout, indent=2))
        file.truncate()
    return redirect('/')
