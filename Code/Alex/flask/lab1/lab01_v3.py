'''
This file is based off of my python file "lab09_unit_converter_v1.py"
'''


import string

from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def unit_converter():

    units_dict = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
    }
    result = ''
    units = ''
    distance = ''


    if request.method == 'POST':
        units = request.form['units']
        distance = float(request.form['distance'])

        if units == "ft" or "feet":
            result = distance * units_dict["ft"]
            units = "ft"
        elif units == "mi" or "miles":
            result = distance * units_dict["mi"]
            units = "mi"
        elif units == "m" or "meters":
            result = distance * units_dict["m"]
            units = "m"
        elif units == "km" or "kilometers":
            result = distance * units_dict["km"]
            units = "km"

    return render_template('index3.html', result=result, units=units, distance=distance)