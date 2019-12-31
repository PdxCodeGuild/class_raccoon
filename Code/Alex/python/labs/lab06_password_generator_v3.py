'''
Lab 6: Password Generator

Version 3 (optional)

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.
'''

import random
import string

#easier interface for the user to use when doing it this way instead of using split function. the user enters a number 4 times instead of a giant string that has to be organized and typed exactly right to work properly.

lowercase_sum = int(input("\n\nHow many lowercase letters would you like in your password?\n"))

uppercase_sum = int(input("\nHow many uppercase letters?\n"))

number_sum = int(input("\nHow many numbers?\n"))

special_char_sum = int(input("\nHow many special characters?\n"))

#I used the variable "password" to represent the empty password.
password = ''

#I used a for loop because i wanted to set a perimeter for each variable of the password. The password "+=" because "for i" needs to be looped until we have the number of characters the user chose.
for i in range(lowercase_sum):
    password += random.choice(string.ascii_lowercase)

for i in range(uppercase_sum):
    password += random.choice(string.ascii_uppercase)

for i in range(number_sum):
    password += random.choice(string.digits)

for i in range(special_char_sum):
    password += random.choice(string.punctuation)

#outro
print("\nYour randomly generated password is displayed below. Good day!")
#password calculated and displayed
print(f"\n\n{password}\n\n\n\n\n\n")
