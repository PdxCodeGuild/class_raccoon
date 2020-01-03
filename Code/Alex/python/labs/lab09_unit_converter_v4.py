'''*not complete*
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
    units = input("What measurement type are we going to convert? (ft, mi, m, km, yd or in)")
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