import random
import os
import string

os.system('cls')

characters = int(input("How many characters long would you like your password? "))
password = ""

while len(password) < characters:
    library = (string.ascii_letters + string.digits + string.punctuation)

    password = password + random.choice(library)

os.system('cls')
print(f"\n\nYou\'re random password is \n\n\n\n{password}\n\n\n")
