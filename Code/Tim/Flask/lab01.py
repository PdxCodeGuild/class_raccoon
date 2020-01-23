from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rotify():
    user_text = ''
    output = ''
    rotation = 13
    indexlist = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if request.method == 'POST':
        user_text = request.form['user_text']
        for i in range(len(user_text)):
            indexlist = alphabet.find(user_text[i]) + rotation
            indexlist %= 26
            output += alphabet[indexlist]
    return render_template('index.html', user_text=user_text, output=output)

@app.route('/passgen', methods=['GET', 'POST'])
def generator():
    passlength = 0
    password = ''
    if request.method == 'POST':
        passlength = int(request.form['passlength'])
        while len(password) < passlength:
            library = (string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "&" + ".")
            password = password + random.choice(library)
    return render_template('index.html', passgen=True, passlength=passlength, password=password)
