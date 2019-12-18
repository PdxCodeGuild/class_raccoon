'''
Filename: helper.py
Author: Dylan
Purpose: simple reusable helper methods
'''

def digit_checker(num,digits = None):
    while True:
        if digits is not None:
            if len(list(num)) > digits:
                print(f"INVALID ENTRY: Entry too large. Please keep to {digits} digits.")
                num = input("> ")
        if num.isdigit():
            return num
        else:
            print("INVALID ENTRY: Enter number ONLY.")
            num = input("> ")