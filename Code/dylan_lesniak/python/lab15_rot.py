'''
Filename: lab15_rot.py
Author: Dylan
Purpose: Create ROT13 cipher
'''

#mods
import string

#functions
def encrypt(code, rotation):
    new_string = ""
    alphabet = string.ascii_lowercase
    #find the index of the letter, add 13 to it, and use mod to loop back to beginning if greater than alphabet length
    for letter in code:
        letter_idx = alphabet.find(letter)
        ciphered_idx = (letter_idx + rotation) % len(alphabet)
        new_string += alphabet[ciphered_idx]
    return new_string

def string_checker(code):
    while True:
        if code.isalpha():
            return code.lower()
        else:
            print("Please enter a valid letter input: ")
            code = input("> ")

def int_checker(rotation):
    while True:
        if rotation.isdigit():
            return int(rotation)
        else:
            print("Please enter a valid integer: ")
            rotation = input("> ")

cont = 'y'
while cont == 'y': 
    print("Encryption Program Start: ")
    print("Please enter the string to be encrypted: ")
    code = string_checker(input("> "))
    print("Please enter the number of rotations you would like: ")
    rotation = int_checker(input("> "))
    print(f"Your encrypted code is: {encrypt(code,rotation)}")
    print("\n Play again? (y/n)")
    cont = input("> ").lower()
