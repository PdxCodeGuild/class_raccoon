from flask import Flask, render_template, request
import random
import string

app =  Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def password():
    output=""
    if request.method == 'POST':
        
        #generate a random password
        #define which parts of ascii I want to use
        password_digits = string.digits
        password_lower = string.ascii_lowercase
        password_upper = string.ascii_uppercase
        password_punctuation = string.punctuation
        #get user input to determine length of password
        number = int(request.form['Numbers'])
        lower = int(request.form['Lowercase'])
        upper = int(request.form['Uppercase'])
        punctuation = int(request.form['Punctuation'])
        #turn those imputs into one string
        output_string = ""
        for num in range(number):
            output_string = output_string + random.choice(password_digits)
        for num in range(lower):
            output_string = output_string + random.choice(password_lower)
        for num in range(upper):
            output_string = output_string + random.choice(password_upper)
        for num in range(punctuation):
            output_string = output_string + random.choice(password_punctuation)
        #shuffle that string
        outputstring_random = list(output_string)
        random.shuffle(outputstring_random)
        output = "".join(outputstring_random)
        #print the final password
    return render_template("index.html", output = output)