'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''



#modules if there were any


#variables
units_dict = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000
}


#save user input
distance = int(input("What is the distance?"))
units = input("What are the units?")


#calculate
if units == "ft":
    result = distance * units_dict["ft"]
elif units == "mi":
    result = distance * units_dict["mi"]
elif units == "m":
    result = distance * units_dict["m"]
elif units == "km":
    result = distance * units_dict["km"]
else:
    print("invalid input")

#print result
print(f"{distance}{units} is {result}m")
