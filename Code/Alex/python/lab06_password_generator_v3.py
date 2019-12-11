'''
Lab 6: Password Generator

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered

input, print
looping
random.choice
the 'sting builder pattern'



Version 3 (optional)

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.
'''

import random
import string

#these are the variables
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
punctuation = string.punctuation
password = '' #this is the literal password
counter = 0 #this line is keeping the loop going
user = input(password)

print("Create a password.")


#generating password with while loop

while counter <= 10: #because we are working with 10 passwords
    password += random.choice(uppercase_letters + lowercase_letters + numbers + punctuation) #this line is randomizing the password and also working with line 14
    counter += 1 #this line is expanding the length of the loop by 1 each time


print(password) #putting this outside of the while loop ensures that the password wont be looped
