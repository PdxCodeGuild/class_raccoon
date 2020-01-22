

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example3/')
def example3():
    name = 'Bill'
    temperature = 40
    return render_template('example3.html', name=name, temperature=temperature, text_color="green")

@app.route('/example4/<int:temperature>/')
def example4(temperature):
    return render_template('example4.html', temperature=temperature)

@app.route('/example5/')
def example5():
    nums = list(range(0, 100))
    return render_template('example5.html', nums=nums)

@app.route('/example6/')
def example6():
    contacts = [{
        'name': 'jim',
        'age': 23,
        'email': 'jim@jim.org',
        'fav_color': 'red'
    },{
        'name': 'jill',
        'age': 234,
        'email': 'jim@jim.org',
        'fav_color': 'blue'
    },{
        'name': 'jane',
        'age': 2345,
        'email': 'jim@jim.org',
        'fav_color': 'green'
    }]
    return render_template('example6.html', contacts=contacts)

@app.route('/example7/', methods=['GET', 'POST'])
def example7():
    response = ''
    temperature = ''
    if request.method == 'POST':
        temperature = request.form['temperature']
        temperature = int(temperature)
        if temperature < 50:
            response = 'cold'
        elif temperature < 80:
            response = 'warm'
        else:
            response = 'hot'
    return render_template('example7.html', temperature=temperature, response=response)

@app.route('/example8/', methods=['GET', 'POST'])
def example8():
    if request.method == 'POST':
        print(request.form)
        mypassword = request.form['mypassword']
        mycheckbox1 = 'mycheckbox1' in response.form

    return render_template('example8.html')

######################### Lab01 unit converter ######################################
# Converse feet to meter
def FeetToMeter(ft):
    return (ft * 0.3048)

# Converse feet to mile
def FeetToMile(ft):
    return (ft * 0.000189394)

# Converse feet to kilometer
def FeetToKilometer(ft):
    return (ft * 0.0003048)

# ==========================
# Converse meter to feet
def MeterToFeet(m):
    return (m * 3.28084)

# Converse meter to mile
def MeterToMile(m):
    return (m * 0.00062137121212121)

# Converse meter to kilometer
def MeterToKilometer(m):
    return (m * 0.001)

# ==========================
# Converse mile to feet
def MileToFeet(mi):
    return (mi * 5280)

# Converse mile to meter
def MileToMeter(mi):
    return (mi * 1609.34)

# Converse mile to kilometer
def MileToKilometer(mi):
    return (mi * 1.60934)

# ==========================
# Converse km to feet
def KilometerToFeet(km):
    return (km * 3280.84)

# Converse km to mile
def KilometerToMile(km):
    return (km * 0.621371)

# Converse km to meter
def KilometerToMeter(km):
    return (km * 1000)

# ==========================
#Rounded decimal to 4
def print4(x):
    return round(x,4)

# ==========================

@app.route('/lab01_unitConverter/', methods=['GET', 'POST'])
def unitConverter():
    num1=''
    num2=''
    unit1=''
    unit2=''
    
    if request.method == 'POST':

        unit1 = request.form['mydropdown']
        unit2 = request.form['mydropdown2']
        num1 = request.form['num1']
        num1 = int(num1)

        if unit1 == 'Feet':
            if unit2 == 'Feet':
                num2 = num1
            elif unit2 == 'Meters':
                num2 = FeetToMeter(num1)
                num2 = print4(num2)
            elif unit2 == 'Miles':
                num2 = FeetToMile(num1)
                num2 = print4(num2)
            elif unit2 == 'Kilometers':
                num2 = FeetToKilometer(num1)
                num2 = print4(num2)

        elif unit1 == 'Meters':
            if unit2 == 'Meters':
                num2 = num1
            elif unit2 == 'Feet':
                num2 = MeterToFeet(num1)
                num2 = print4(num2)
            elif unit2 == 'Miles':
                num2 = MeterToMile(num1)
                num2 = print4(num2)
            elif unit2 == 'Kilometers':
                num2 = MeterToKilometer(num1)
                num2 = print4(num2)

        elif unit1 == 'Miles':
            if unit2 == 'Miles':
                num2 = num1
            elif unit2 == 'Feet':
                num2 = MileToFeet(num1)
                num2 = print4(num2)
            elif unit2 == 'Meters':
                num2 = MileToMeter(num1)
                num2 = print4(num2)
            elif unit2 == 'Kilometers':
                num2 = MileToKilometer(num1)
                num2 = print4(num2)

        elif unit1 == 'Kilometers':
            if unit2 == 'Kilometers':
                num2 = num1
            elif unit2 == 'Feet':
                num2 = KilometerToFeet(num1)
                num2 = print4(num2)
            elif unit2 == 'Meters':
                num2 = KilometerToMeter(num1)
                num2 = print4(num2)
            elif unit2 == 'Miles':
                num2 = KilometerToMile(num1)
                num2 = print4(num2)

    return render_template("lab01_unitConverter.html", unit1=unit1, unit2=unit2, num1 = num1, num2 = num2)

##################################################################################################################
