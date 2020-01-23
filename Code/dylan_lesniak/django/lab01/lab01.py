from flask import Flask, render_template, request
import string
import random
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

#look up patterns for the input method
#flask
@app.route('/rot/', methods=['GET', 'POST'])
def rot():
    response = ''
    cypher = ''
    rotations = 0 
    if request.method == 'POST':
        cypher = request.form['cypher']
        rotations = request.form['rotations']
        rotations = int(rotations)
        cypher = encrypt(cypher, rotations)
        response = cypher
    return render_template('rot.html', cypher=cypher, response=response)

@app.route('/password/', methods=['GET', 'POST'])
def passwrd(): 
    response = ''
    lower_count = 0 
    upper_count = 0 
    number_count = 0 
    spec_count = 0 
    password = ""
    enc_pass = ""
    if request.method == 'POST':
        lower_count = int(request.form['lower_count'])
        upper_count = int(request.form['upper_count'])
        number_count = int(request.form['number_count'])
        spec_count = int(request.form['spec_count'])
        password = generate(lower_count,upper_count,number_count,spec_count)
        enc_pass = "".join(["*" for letter in password])
        response = True
    return render_template('password.html', lower_count=lower_count, upper_count=upper_count,number_count=number_count,spec_count=spec_count,password=password, enc_pass=enc_pass, response=response)
    # lower_count,upper_count,number_count,spec_count

@app.route('/unit/', methods=['GET','POST'])
def unit():
    response = ''
    unit_from = ""
    unit_to = ""
    amount_from = 0 
    amount_to = 0
    if request.method == 'POST':
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']
        amount_from = int(request.form['amount_from'])
        amount_to = convert(unit_from,unit_to,amount_from)
        response = True
    return render_template('unit.html', unit_from=unit_from, unit_to=unit_to, amount_from=amount_from, amount_to=int(amount_to), response=response)


#methods
def encrypt(code, rotation = 13):
    new_string = ""
    alphabet = string.printable
    #find the index of the letter, add 13 to it, and use mod to loop back to beginning if greater than alphabet length
    for letter in code:
        letter_idx = alphabet.find(letter)
        ciphered_idx = (letter_idx + rotation) % len(alphabet)
        new_string += alphabet[ciphered_idx]
    return new_string

def generate(lower_count,upper_count,number_count,spec_count):
    password = ""
    lows = string.ascii_lowercase
    ups = string.ascii_uppercase
    nums = string.digits
    special = string.punctuation
    for x in range(lower_count):
        password += random.choice(lows)
    for x in range(upper_count):
        password += random.choice(ups)
    for x in range(number_count):
        password += random.choice(nums)
    for x in range(spec_count):
        password += random.choice(special)
    pass_list = list(password)
    random.shuffle(pass_list)
    password = "".join(pass_list)
    return password

def convert(unit_from,unit_to,amount_from):
    #how many meters is each unit
    type_hash = {"Inches":1/39.37,"Feet":1/3.281,"Yards":1/1.094,"Miles":(1609.34),"Meters":1,"Kilometers":(1000)}
    meters = type_hash[unit_from] * amount_from
    if unit_from == "Meters":
        return meters
    else:
        return meters // type_hash[unit_to]