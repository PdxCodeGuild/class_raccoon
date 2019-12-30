# lab09_unit.py

# dictionary
units_dict = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}


# save user input
distance = int(input("What is the distance to meters? "))
units = input("Is this 'ft', 'mi', 'm', or 'km': ")

# calculate
if units not in units_dict.keys():
    print("Invalid input.")
else:
    result = distance * units_dict[units]
    print(f"{distance}{units} is {result}m")
