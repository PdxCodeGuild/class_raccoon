import random
import os
import string

os.system('cls')

characters = int(input("How many characters long would you like your password? "))
password = ""

while len(password) < characters:
    #original library of characters
    # library = (string.ascii_letters + string.digits + string.punctuation)

    #library of characters with most common special characters
    library = (string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "&" + ".")
    password = password + random.choice(library)

os.system('cls')
print(f"\n\nYou\'re random password is: \n\n\n\n{password}\n\n\n\nDon\'t lose it!\n\n\n")
