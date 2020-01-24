from flask import Flask, render_template, request
import string

app = Flask(__name__)

def cipher(num, alphabet):
    rotalpha = alphabet[num:] + alphabet[0:num]
    return rotalpha

@app.route('/', methods=['GET', 'POST'])
def index():
    passphrase = ''
    keyphrase = ''
    dist = ''
    unit = ''
    enunit = ''
    conversion = ''
    if request.method == 'POST':
        if 'keyphrase' in request.form:
            keyphrase = request.form['keyphrase']
            passphrase = rot13(keyphrase)
        elif 'dist' in request.form and 'unit' in request.form:
            dist = request.form['dist']
            unit = request.form['unit']
            if 'enunit' in request.form:
                enunit = request.form['enunit']
                conversion = unitconv(dist, unit, enunit)
    return render_template('index.html', passphrase=passphrase, dist=dist, unit=unit, enunit=enunit, conversion=conversion)

def rot13(keyphrase):
    alphabet = string.ascii_lowercase
    rotalpha = cipher(13, alphabet)
    alphabet = list(alphabet)
    rotalpha=list(rotalpha)
    passphrase = ""

    for i in keyphrase:
        if i in alphabet:
            passphrase += rotalpha[alphabet.index(i)]
        else:
            passphrase += i

    print("Here's your encoded text:")
    return passphrase

def unitconv(dist, unit, enunit):
    meters = {
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000
    }

    dist = int(dist)

    conversion = round(dist*meters[unit]*(1/meters[enunit]), 2)

    return conversion