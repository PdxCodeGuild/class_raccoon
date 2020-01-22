from flask import Flask, render_template, request
import string
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

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

@app.route('/', methods=['GET', 'POST'])
def passwrd(): 
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

def encrypt(code, rotation = 13):
    new_string = ""
    alphabet = string.ascii_lowercase
    #find the index of the letter, add 13 to it, and use mod to loop back to beginning if greater than alphabet length
    for letter in code:
        letter_idx = alphabet.find(letter)
        ciphered_idx = (letter_idx + rotation) % len(alphabet)
        new_string += alphabet[ciphered_idx]
    return new_string