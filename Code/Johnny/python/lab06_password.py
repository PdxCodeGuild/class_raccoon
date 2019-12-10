# lab06_password.py
"""
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered

input, print
looping
random.choice
the 'sting builder pattern'
"""
# import modules to use
import string
import random

# define prompt/strings/variables
options = string.ascii_letters + string.digits + string.punctuation
user_var = input("How many characters do you want your password? ")

# try check value errors if letters are presents
try:
    val = int(user_var)
    give_pass = ""
    for x_pass in range (0, int(user_var)):
        give_pass = give_pass + random.choice(options)
        give_pass = give_pass + ""
    print(f"Here is your {user_var} character password: {give_pass} \n")
except ValueError:
    print("That's not a number. ")
