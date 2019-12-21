'''
Filename: helper.py
Author: Dylan
Purpose: simple reusable helper methods
'''

import string

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

def text_checker(text,acceptable_inputs = []):
    ok_formats = f"{string.ascii_letters},{string.whitespace}"
    text = text.lower()
    while True:
        if all([char for char in text if char in ok_formats]):
            if len(acceptable_inputs) > 0:
                print()
                if any([option for option in acceptable_inputs if text.lower() in option.lower()]):
                    return text
                else:
                    print(f"INVALID ENTRY: Entry not in list.")
                    if len(acceptable_inputs) <= 20:
                        print(f"You entered: {text}")
                        print(f"Acceptable inputs are: {acceptable_inputs}")
                    text = input("> ")
            else:
                return text
        else:
            print("INVALID ENTRY: Please enter valid text entry. ")
            text = input("> ")

def time_checker(num):
    while True:
        num_list = list(num)
        first_half = num_list[:2]
        second_half = num_list[3:]
        if len(num_list) != 5:
            print("INVALID ENTRY: Please enter time in this format: '00:00'.")
            num = input("> ")
        elif num_list[2] != ":":
            print("INVALID ENTRY: Please enter time in this format: '00:00'.")
            num = input("> ")
        elif not all([x.isdigit() for x in first_half]) and not all([x.isdigit() for x in second_half]):
            print(num_list)
            print("INVALID ENTRY: Please enter time in this format: '00:00'.")
            num = input("> ")
        elif int("".join(first_half)) > 24:
            print("INVALID ENTRY: Please enter time in a 12 or 24 hour format.")
            num = input("> ")
        elif int("".join(second_half)) > 59:
            print("INVALID ENTRY: Please enter time with minutes from '00 to 59'.")
            num = input("> ")
        else:
            return [first_half, second_half]
        




'''
def add(a, b):
    return a + b

add = lambda a, b: a + b


nums = ['5', '56', '986']
print(all([x.isdigit() for x in nums]))


nums = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6...]



# nums = [5, 6, 7]
# nums.sort()

# nums = [(5, 'a'), (6, 'b'), (7, 'd')]
# nums.sort(key=lamda x: x[0])
'''