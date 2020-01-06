'''
Lab 9: Unit Converter

Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
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
    units = input(f"What measurement are we working with? ")
    distance = input(f"How many {units}? ")
    for char in distance:
        if char not in string.digits and char != ".":
            print("The units have to be a number.")
            break
        else:
            distance = float(distance)
#calculating units
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
    else:
        print("invalid input")

    print(f"{distance}{units} is {result}m")
    input('')

