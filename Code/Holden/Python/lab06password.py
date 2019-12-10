import random
import string
while True:
    lower_in=input("How many lower case letters do you want in the password? ")
    try:
        lower=int(lower_in)
        if lower >= 0:
            break
        else:
            print("Please enter a valid positive integer.")
    except ValueError:
        print("Please enter a valid integer.")
while True:
    upper_in=input("How many upper case letters do you want in the password? ")
    try:
        upper=int(upper_in)
        if upper >= 0:
            break
        else:
            print("Please enter a valid positive integer.")
    except ValueError:
        print("Please enter a valid integer.")
while True:
    number_in=input("How many numerical symbols do you want in the password? ")
    try:
        number=int(number_in)
        if number >=0:
            break
        else:
            print("Please enter a valid positive integer.")
    except ValueError:
        print("Please enter a valid integer.")
while True:
    symb_in=input("How many special characters do you want in the password? ")
    try:
        symb=int(symb_in)
        if symb >=0:
            break
        else:
            print("Please enter a valid positive integer.")
    except ValueError:
        print("Please enter a valid integer.")
output = ""
while lower > 0:
    output+= random.choice(string.ascii_lowercase)
    lower -= 1
while upper > 0:
    output+= random.choice(string.ascii_uppercase)
    upper -= 1
while number > 0:
    output+= str(random.randint(1,9))
    number -= 1
while symb > 0:
    output+= random.choice(string.punctuation)
    symb -= 1
output=list(output)
random.shuffle(output)
prntstr=""
prntstr=prntstr.join(output)
print(prntstr)
