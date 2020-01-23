'''
Lab 9: Unit Converter

Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

ft	mi	m	km
ft	1		0.3048
mi		1	1609.34
m	1/0.3048	1/1609.34	1	1/1000
km			1000	1
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
'''


import os
import string




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
    return None


units_dict = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yd": 0.9144,
"in": 0.0254
}

while True:
    os.system("clear")

    text = input('Enter your conversion (5 miles to inches): ')
    text = text.split(' ')
    distance = text[0]
    input_units = text[1]
    output_units = text[3]

    distance = float(distance)
    input_units = check_units(input_units)
    output_units = check_units(output_units)
    if input_units == None or output_units == None:
        print('invalid units')
        exit()

    output_distance = distance*units_dict[input_units]/units_dict[output_units]
    output_distance = round(output_distance, 4)
    print(f'{distance} {input_units} is {output_distance} {output_units}')

