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

def print4(x):
    print(round(x,4))

converse_again = 'y'

while converse_again == 'y':
    user_input = float(input('what is the distance?(number) '))
    unit_input = input('what are the input units?(ft, m, mi, km)').lower()
    unit_output = input('what are the output units?(ft, m, mi, km)').lower()

    if unit_input == 'ft':
        if unit_output == 'ft':
            print('1')
        elif unit_output == 'm':
            print4(FeetToMeter(user_input))
        elif unit_output == 'mi':
            print4(FeetToMile(user_input))
        elif unit_output == 'km':
            print4(FeetToKilometer(user_input))

    elif unit_input == 'm':
        if unit_output == 'ft':
            print4(MeterToFeet(user_input))
        elif unit_output == 'm':
            print('1')
        elif unit_output == 'mi':
            print4(MeterToMile(user_input))
        elif unit_output == 'km':
            print4(MeterToKilometer(user_input))

    elif unit_input == 'mi':
        if unit_output == 'ft':
            print4(MileToFeet(user_input))
        elif unit_output == 'm':
            print4(MileToMeter(user_input))
        elif unit_output == 'mi':
            print('1')
        elif unit_output == 'km':
            print4(MileToKilometer(user_input))

    elif unit_input == 'km':
        if unit_output == 'ft':
            print4(KilometerToFeet(user_input))
        elif unit_output == 'm':
            print4(KilometerToMeter(user_input))
        elif unit_output == 'mi':
            print4(KilometerToMile(user_input))
        elif unit_output == 'km':
            print('1')

    converse_again = input('Do it again?(y/n)').lower()
else:
    print('See you again!')
