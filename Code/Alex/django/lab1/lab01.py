import random
import string

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    nums = ''
    password = ''


    # if request.
    if request.method == 'POST':
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        numbers = string.digits
        punctuation = string.punctuation
        nums = request.form['nums']
        nums = int(nums)

        for i in range(nums):
            password += random.choice(uppercase_letters + lowercase_letters + numbers + punctuation)




    return render_template('index.html', nums=nums, password=password)