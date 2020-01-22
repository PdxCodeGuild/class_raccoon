'''
Filename: lab09_unit_conversion.py
Author: Dylan
Purpose: Convert imperial and metric units
'''

def convert():
    #how many meters is each unit
    type_hash = {"in":1/39.37,"ft":1/3.281,"yd":1/1.094,"mi":(1609.34),"m":1,"km":(1000)}
    start_type = get_start_type()
    start_amount = get_start_amount()
    end_type = get_end_type()
    meters = type_hash[start_type] * start_amount
    if start_type == "m":
        return round(meters,2)
    else:
        return round(meters / type_hash[end_type],2)
    

def get_start_type():
    print(f"""Welcome to the Unit Converter. You can convert from any of the following to any other unit in the list: ")
Inches (in), feet (ft), yards (yd), miles (mi), meters (m), or kilometers (km).
Please enter the the starting unit type: (in, ft, yd, mi, m, km)""")
    start_type = unit_checker(input("> "))
    return start_type

def get_start_amount():
    print("Please enter the unit amount: (any integer)")
    start_amount = digit_checker(input("> "))
    return start_amount

def get_end_type():
    print("Please enter the desired unit type: (in, ft, yd, mi, m, km)")
    end_type = unit_checker(input("> "))
    return end_type

def unit_checker(unit):
    possible_inputs = ["in", "ft", "yd", "mi", "m", "km"]
    while True:
        if unit not in possible_inputs:
            print("Please enter a valid unit type: (in, ft, yd, mi, m, km)")
            unit = input("> ")
        else:
            return unit.lower()

def digit_checker(num):
    while True:
        if num.isdigit():
            return int(num)
        else:
            print("Please enter a valid integer: ")
            num = input("> ")

cont = "y"
while cont == "y":
    print(convert())
    print("\nWould you like to convert a new value? (y/n)")
    cont = input("> ").lower()