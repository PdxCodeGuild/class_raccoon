'''
Lab 6: Password Generator

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered

input, print
looping
random.choice
the 'sting builder pattern'
'''

#i need the random module to GENERATE randomness into the password calculation
#i need to import string to GENERATE the string libraries within my code
import random
import string

#i need all password options. so i created variables representing each individual library of strings that i need.
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
punctuation = string.punctuation
password = '' #because i am dealing with strings

counter = 0 #this lines purpose is to keep the loop going

#using while loop to keep counter going
while counter <= 10: #because we need 10 passwords
    password += random.choice(uppercase_letters + lowercase_letters + numbers + punctuation) #the password calculation. adding and combining the blank string with the calculation for the password
    counter += 1 #this variable within the loop is incrimenting/adding 1 to the counter each time through the loop so that we get to 10 passwords one by one

print(password) #putting this outside of the while loop ensures that the password wont be looped
