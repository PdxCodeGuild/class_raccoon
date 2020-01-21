from flask import Flask, render_template, request
import string
import random
app = Flask(__name__)

# to run, type export 'FLASK_APP=testingflask.py' or replace testingflask with local file.
# then type 'flask run' or 'python -m flask run'
# to set flask in development type 'export FLASK_ENV=development'
@app.route('/', methods=['GET', 'POST'])
def index():
    password_length = ''
    if request.method == 'POST':
        password_length = request.form['password_length']
        password_length = int(password_length)
        for x in range(0, int(password_length)):
            print(x)
    print(request.form)
    return render_template('index.html', password_length=password_length)
