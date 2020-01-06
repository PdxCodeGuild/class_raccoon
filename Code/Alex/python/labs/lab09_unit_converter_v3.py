'''
Lab 9: Unit Converter

Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
'''


import os
import string


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
    units = input("What measurement are we working with? ")
    distance = input(f"How many? ")
    for char in distance:
        if char not in string.digits and char != ".":
            print("The units have to be a number.")
            break
        else:
            distance = float(distance)
#calculating units
    if units == "ft" or units == "feet" or units == "foot":
        result = distance * units_dict["ft"]
        units = "ft"
    elif units == "mi" or units == "miles" or units == "mile":
        result = distance * units_dict["mi"]
        units = "mi"
    elif units == "m" or units == "meters" or units == "meter":
        result = distance * units_dict["m"]
        units = "m"
    elif units == "km" or units == "kilometers" or units == "kilometer":
        result = distance * units_dict["km"]
        units = "km"
    elif units == "yd" or units == "yards" or units == "yard":
        result = distance * units_dict["yd"]
        units = "yd"
    elif units == "in" or units == "inches" or units == "inch":
        result = distance * units_dict["in"]
        units = "in"
    else:
        print("invalid input")

    print(f"{distance}{units} is {result}m")
    input('')