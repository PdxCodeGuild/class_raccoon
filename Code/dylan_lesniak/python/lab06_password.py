'''
Filename: lab06_password.py
Author: Dylan
Purpose: Creates a randomly generated password. Takes user input for how many special characters. 
'''

#mods
import random 
import string

#variables
lows = string.ascii_lowercase
ups = string.ascii_uppercase
nums = string.digits
special = string.punctuation

#functions
def create_pass():
    print("Welcome to MAXIMUM SECURITY! Your stop for passwords.")
    print("How many lowercase letters would you like?")
    lower_count = int(input_checker(input("> ")))
    print("How many uppercase letters would you like?")
    upper_count = int(input_checker(input("> ")))
    print("How many numbers would you like?")
    number_count = int(input_checker(input("> ")))
    print("Lastly, how many special characters would you like?")
    spec_count = int(input_checker(input("> ")))
    password = generate(lower_count,upper_count,number_count,spec_count)
    print("Your password is: ")
    print(f"{password}")

def generate(lower_count,upper_count,number_count,spec_count):
    password = ""
    for x in range(lower_count):
        password += random.choice(lows)
    for x in range(upper_count):
        password += random.choice(ups)
    for x in range(number_count):
        password += random.choice(nums)
    for x in range(spec_count):
        password += random.choice(special)
    pass_list = list(password)
    random.shuffle(pass_list)
    password = "".join(pass_list)

    return password

    
def input_checker(num):
    while True:
        if num.isdigit():
            return num
        else:
            print("Please enter a valid number.")
            num = input("> ")

cont = "y"
while cont == "y":
    create_pass()
    print("Would you like to create another password? (y/n)")
    cont = input("> ").lower()

print("Thank you for using MAXIMUM SECURITY! Where we take security, to the MAX!")