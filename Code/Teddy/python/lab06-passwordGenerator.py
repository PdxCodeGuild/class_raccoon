# Lab 6: Password Generator
# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

import random
import string

print('Welcome to password generation program')

# Ask the user for how many lowercase letters, uppercase letters, numbers,
# and special characters they'd like in their password.
uppercase_letters =  int(input('How many Uppercase letters? '))

lowercase_letters = int(input('How many Lowercase letters? '))

numbers = int(input('How many numbers? '))

special_characters = int(input('How many Special characters? '))

output_upper = ''
output_lower = ''
output_number = ''
output_special = ''

for i in range(uppercase_letters):
    output_upper += random.choice(string.ascii_letters).upper()
# print(output_upper)

for i in range(lowercase_letters):
    output_lower += random.choice(string.ascii_letters).lower()
# print(output_lower)

for i in range(numbers):
    output_number += random.choice(string.digits)
# print(output_number)

for i in range(special_characters):
    output_special += random.choice(string.punctuation)
# print(output_special)

# Concaternate together and delete
output = output_upper + output_lower + output_number + output_special
# print(output)

# Converse to list
output_list = list(output)

# Shuffle list
random.shuffle(output_list)

# Join together as string
output_string = ''.join(output_list)
print(f'Your password is {output_string}')
