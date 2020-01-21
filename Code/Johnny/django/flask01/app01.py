from flask import Flask
app = Flask(__name__)

# to run, type export 'FLASK_APP=testingflask.py' or replace testingflask with local file.
# then type 'flask run' or 'python -m flask run'
# to set flask in development type 'export FLASK_ENV=development'
@app.route('/')
def hello_world():
    return 'Hello World!'
