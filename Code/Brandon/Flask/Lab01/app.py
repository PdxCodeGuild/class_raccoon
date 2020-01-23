from flask import Flask, request, render_template
app = Flask(__name__)

def unit_convert(measurement,x):
    unit_dict = { "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000}

    if x == "feet":
        user_1 = measurement * unit_dict["ft"]
        return float(user_1)
    elif x == "mile":
        user_1 = measurement * unit_dict["mi"]
        return float(user_1)
    elif x == "meter":
        user_1 = measurement * unit_dict["m"]
        return float(user_1)
    elif x == "kilometer":
        user_1= measurement * unit_dict["km"]
        return float(user_1)

def conversion2(user_1, y):
    unit_dict = { "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000}
    
    if y == "meter":
        user_2 = user_1 / unit_dict["m"]
        return(f"{user_2} meters")
    elif y == "feet":
        user_2 = user_1 / unit_dict["ft"]
        return(f"{user_2} feet")
    elif y == "mile":
        user_2 = user_1 / unit_dict["mi"]
        return(f"{user_2} miles")
    elif y == "kilometer":
        user_2 = user_1 / unit_dict["km"]
        return(f"{user_2} kilometer")

@app.route('/', methods=["GET", "POST"])
def index():
    measurement =""
    unit=""
    values = ""
    if request.method == "POST":
        measurement = request.form["measurement"]
        measurement = float(measurement)
        unit = request.form["unit"]
        values = unit_convert(measurement,unit)
    data = {
        'values': values,
        'measurement': measurement,
        'unit': unit
    }
    return render_template("index.html",**data) 

@app.route('/choice', methods=["GET", "POST"])
def unitto():
    measurement =""
    unit=""
    values = ""
    new_values = ""
    unit_to = ""
    if request.method == "POST":
        measurement = request.form["measurement"]
        measurement = float(measurement)
        unit = request.form["unit"]
        unit_to = request.form["unit_to"]
        values = unit_convert(measurement,unit)
        new_values = conversion2(values, unit_to)
    data = {
        'measurement': measurement,
        'unit': unit,
        'unit_to': unit_to,
        'new_values':new_values 
    }
    return render_template("index2.html",**data) 
