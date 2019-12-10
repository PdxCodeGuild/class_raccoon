#generate a random password
import random
import string
#define which parts of ascii I want to use
password_digits = string.digits
password_lower = string.ascii_lowercase
password_upper = string.ascii_uppercase
password_punctuation = string.punctuation
#get user input to determine length of password
number = input("How many numbers would you like? ")
number = int(number)
lower = input("How many lowercase letters would you like? ")
lower = int(lower)
upper = input("How many uppercase letters would you like?")
upper = int(upper)
punctuation = input("How many punctuation marks would you like?")
punctuation = int(punctuation)
#turn those imputs into one string
output_string = ""
for num in range(number):
    output_string = output_string + random.choice(password_digits)
for num in range(lower):
    output_string = output_string + random.choice(password_lower)
for num in range(upper):
    output_string = output_string + random.choice(password_upper)
for num in range(punctuation):
    output_string = output_string + random.choice(password_punctuation)
#shuffle that string
outputstring_random = list(output_string)
random.shuffle(outputstring_random)
output = "".join(outputstring_random)
#print the final password
print(output)
