# lab15_rot.py

# importing modules to use, in this instance, 'string'
import string

# string with the ascii lowercase
rot = string.ascii_lowercase

# prompt for input
user_input = input("Enter something to encrypt: ")

user_output = ""
for i in user_input:
    user_output += rot[(rot.find(i)+13)%len(rot)]
print(user_output)
