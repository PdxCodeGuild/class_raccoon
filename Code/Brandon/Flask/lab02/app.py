from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)


def save_database(data):
    # '''Saving database function'''
    with open('data.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    # '''Database loading function'''
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
    return data



@app.route('/')
def index():
    # '''This is the initial page that will be loaded'''
    data = load_database()
    data = data['todos']
    return render_template('index.html',data=data)
    

@app.route('/post/',methods=["POST"])
def add():
    '''
    ---Explantion of the task addition---

    This function will all the user to add a task to the todo list. data = load database, loads the json doc then we take the items from the dictionary and place them into a list. priority and add take the form data and turn it into a response. We append those to the list, save it to the json and use the redirect to return to the previous page

    '''
    data = load_database()
    data = data['todos']
    priority = request.form["priority"]
    add = request.form["add"]
    data.append({"text":add, "priority":priority})#apends the values to the keys in a dictionary, and puts them in the list
    save_database({"todos":data}) #takes the data saved to the list(todos) and calls the save function.
    return redirect('/') #--Redirects to the main app route page

@app.route('/delete/', methods=['POST'])
def delete():
    data = load_database()
    data = data['todos']
    if request.form['remove'] == 'done':
        for i in range(len(data)):
            if data[i]["text"] == request.form['name']:
                data[i]['priority'] = 'done'
                save_database({"todos":data})
                break
    elif request.form['remove'] == 'remove':
        for i in range(len(data)):
            if data[i]["text"] == request.form['name']:
                data.pop(i)
                save_database({"todos":data})
                break
    return redirect('/')



        



    