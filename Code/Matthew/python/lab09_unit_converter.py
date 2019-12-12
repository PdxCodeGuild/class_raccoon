

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


units = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}
#
# distance = input('What is the distance? ')
# input_units = input('What are the input units? ')
# output_units = input('What are the output units? ')

text = input('Enter your conversion (5 miles in inches): ')
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

output_distance = distance*units[input_units]/units[output_units]
output_distance = round(output_distance, 4)
print(f'{distance} {input_units} is {output_distance} {output_units}')
