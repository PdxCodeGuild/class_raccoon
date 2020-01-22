'''
This lab is based off my python lab6_v3 file
'''

import random
import string

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index2():
    nums = ''
    password = ''


    # if request.
    if request.method == 'POST':
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        numbers = string.digits
        punctuation = string.punctuation
        lowercase = int(request.form['lowercase'])
        uppercase = int(request.form['uppercase'])
        nums = int(request.form['nums'])
        special_char = int(request.form['special_char'])


        for i in range(lowercase):
            password += random.choice(lowercase_letters)
        for i in range(uppercase):
            password += random.choice(uppercase_letters)
        for i in range(nums):
            password += random.choice(numbers)
        for i in range(special_char):
            password += random.choice(punctuation)

        password = list(password)
        random.shuffle(password)
        password = ''.join(password)


    return render_template('index2.html', password=password)