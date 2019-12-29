# lab09_unit.py

# dictionary
units_dict = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}


# save user input
distance = int(input("What is the distance: "))
units = input("Is this 'ft', 'mi', 'm', or 'km': ")
units2 = input('Convert to what unit: ')

# calculate
if units not in units_dict.keys():
    print("Invalid input.")
else:
    result = distance * units_dict[units]
    out_unit = result/units_dict[units2]
    print(f'{distance} {units} is equal {out_unit} {units2}.')
