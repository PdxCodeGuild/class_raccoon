#Random password generator, Brandon G.

import random
import string



def randompass():
    length = user_input
    avail_chars = string.ascii_letters + string.punctuation + string.digits
    password = ""
    for i in range(length):
        password += random.choice(avail_chars)
    print(password)


print("This will create a random password for you.")
user_input = input("How many characters?")
user_input = int(user_input)
randompass()

# print("Next chose what chars you want.\n")
# upper = input("How many uppercase letters?")
# upper = input("How many uppercase letters?")
# upper = input("How many uppercase letters?")
# upper = input("How many uppercase letters?")
