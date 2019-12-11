'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

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




#modules if there were any

#variables
units_dict = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yd": 0.9144,
"in": 0.0254
}


#save user input
distance = int(input("What is the distance?"))
units = input("What are the units?")


#calculate
if units not in units_dict.keys():
    print("invalid input")
else:
    result = distance * units_dict[units]


#Alternate calculate
#if units == "ft":
#    result = distance * units_dict["ft"]
#elif units == "mi":
#    result = distance * units_dict["mi"]
#elif units == "m":
#    result = distance * units_dict["m"]
#elif units == "km":
#    result = distance * units_dict["km"]
#elif units == "yd":
#    result = distance * units_dict["yd"]
#elif units == "in":
#    result = distance * units_dict["in"]
#else:
#    print("invalid input")


#print result
print(f"{distance}{units} is {result}m")
