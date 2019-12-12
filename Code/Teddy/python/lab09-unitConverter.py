# Lab 9: Unit Converter

# Converse feet to meter
def FeetToMeter(ft):
    return (ft * 0.3048)

# Converse feet to mile
def FeetToMile(ft):
    return (ft * 0.000189394)

# Converse feet to kilometer
def FeetToKilometer(ft):
    return (ft * 0.0003048)

# =====================================
# Converse meter to feet
def MeterToFeet(m):
    return (m * 3.28084)

# Converse meter to mile
def MeterToMile(m):
    return (m * 0.00062137121212121)

# Converse meter to kilometer
def MeterToKilometer(m):
    return (m * 0.001)

# =====================================
# Converse mile to feet
def MileToFeet(mi):
    return (mi * 5280)

# Converse mile to meter
def MileToMeter(mi):
    return (mi * 1609.34)

# Converse mile to kilometer
def MileToKilometer(mi):
    return (mi * 1.60934)

# =====================================
# Converse km to feet
def KilometerToFeet(km):
    return (km * 3280.84)

# Converse km to mile
def KilometerToMile(km):
    return (km * 0.621371)

# Converse km to meter
def KilometerToMeter(km):
    return (km * 1000)

# =====================================

# User input in feet
# input_feet = float(input('What is the distance in feet?'))
# answerFeetMeter = float(round(FeetToMeter(input_feet), 4))
# answerFeetMile = float(round(FeetToMile(input_feet), 4))
# answerFeetKilometer = float(round(FeetToKilometer(input_feet), 4))

# print(f'{input_feet} ft. = {answerFeetMeter} m. = {answerFeetMile} mi. = {answerFeetKilometer} km.')

# User input in meter
# input_meter = float(input('What is the distance in meter?'))
# answerMeterFeet = float(round(MeterToFeet(input_meter), 4))
# answerMeterMile = float(round(MeterToMile(input_meter), 4))
# answerMeterKilometer = float(round(MeterToKilometer(input_meter), 4))

# print(f'{input_meter} m. = {answerMeterFeet} ft. = {answerMeterMile} mi. = {answerMeterKilometer} km.')

# User input in mile
# input_mile = float(input('What is the distance in mile?'))
# answerMileFeet = float(round(MileToFeet(input_mile), 4))
# answerMileMeter = float(round(MileToMeter(input_mile), 4))
# answerMileKilometer = float(round(MileToKilometer(input_mile), 4))

# print(f'{input_mile} mi. = {answerMileFeet} ft. = {answerMileMeter} m. = {answerMileKilometer} km.')

# User input in kilometer
# input_kilometer = float(input('What is the distance in kilometer?'))
# answerKilometerFeet = float(round(KilometerToFeet(input_kilometer), 4))
# answerKilometerMile = float(round(KilometerToMile(input_kilometer), 4))
# answerKilometerMeter = float(round(KilometerToMeter(input_kilometer), 4))

# print(f'{input_kilometer} km. = {answerKilometerFeet} ft. = {answerKilometerMile} mi. = {answerKilometerMeter} m.')





converse_again = 'y'

while converse_again == 'y':
    user_input = float(input('what is the distance?(number) '))
    unit_input = input('what are the input units?(ft, m, mi, km)').lower()
    unit_output = input('what are the output units?(ft, m, mi, km)').lower()

    if unit_input == 'ft':
        if unit_output == 'ft':
            print('1')
        elif unit_output == 'm':
            print(FeetToMeter(user_input))
        elif unit_output == 'mi':
            print(FeetToMile(user_input))
        elif unit_output == 'km':
            print(FeetToKilometer(user_input))

    elif unit_input == 'm':
        if unit_output == 'ft':
            print(MeterToFeet(user_input))
        elif unit_output == 'm':
            print('1')
        elif unit_output == 'mi':
            print(MeterToMile(user_input))
        elif unit_output == 'km':
            print(MeterToKilometer(user_input))

    elif unit_input == 'mi':
        if unit_output == 'ft':
            print(MileToFeet(user_input))
        elif unit_output == 'm':
            print(MileToMeter(user_input))
        elif unit_output == 'mi':
            print('1')
        elif unit_output == 'km':
            print(MileToKilometer(user_input))

    elif unit_input == 'km':
        if unit_output == 'ft':
            print(KilometerToFeet(user_input))
        elif unit_output == 'm':
            print(KilometerToMeter(user_input))
        elif unit_output == 'mi':
            print(KilometerToMile(user_input))
        elif unit_output == 'km':
            print('1')

    converse_again = input('Do it again?(y/n)').lower()
else:
    print('See you again!')
