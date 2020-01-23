'''
This file is based off of my python file "lab09_unit_converter_v4.py"
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
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
    }

    result = ''
    units = ''
    distance = ''
    input_units = ''
    output_units = ''
    output_distance = ''


    if request.method == 'POST':

        def check_units(units):
            if units in ['feet', 'feets', 'ft', 'foot']:
                return 'ft'
            elif units in ['mile', 'miles', 'mi']:
                return 'mi'
            elif units in ['meter', 'meters', 'm']:
                return 'm'
            elif units in ['kilometer', 'kilometers', 'km']:
                return 'km'
            elif units in ['yard', 'yards', 'yd']:
                return 'yd'
            elif units in ['inch', 'inches', 'in']:
                return 'in'
            else: return None

        units = request.form['units']
        units = units.split(' ')
        distance = units[0]
        distance = float(distance)
        input_units = units[1]
        input_units = check_units(input_units)
        output_units = units[3]
        output_units = check_units(output_units)

        output_distance = distance*units_dict[input_units]/units_dict[output_units]
        output_distance = round(output_distance, 4)



    return render_template('index4.html', distance=distance, input_units=input_units, output_units=output_units, output_distance=output_distance)



