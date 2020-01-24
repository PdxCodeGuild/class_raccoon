from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

@app.route('/')
def todo():
    todo_list = []
    with open(r"lab02\database.json", "r") as file:
        data = json.loads(file.read())
    for item in data["todos"]:
        todo_list.append(item["text"])
    return render_template('lab02todo.html', todo_list=todo_list)

@app.route('/save/', methods=['POST'])
def database_save():
    todo_list = []
    with open(r"lab02\database.json", "r+") as file:
        data = json.loads(file.read())
        new_todo = request.form["new_todo"]
        not_in_list = True
        dataout = {"todos": []}
        for item in data["todos"]:
            if item["text"] not in request.form:
                dataout["todos"].append(item)
            if item["text"] == new_todo:
                not_in_list = False
        if not_in_list and new_todo:
            dataout["todos"].append({"text": new_todo})
        file.seek(0)
        file.write(json.dumps(dataout))
        file.truncate()
    return redirect('/')
