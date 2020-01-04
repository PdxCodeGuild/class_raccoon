'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.


Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''


import os
import string


units_dict = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000
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