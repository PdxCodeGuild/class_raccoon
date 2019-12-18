#lab15_rot_ver3.py
import string
import random

print("True substitution cipher!")

#create a list of all displayable characters
allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
print(allchar)

#function for using seed to generate cipher
def cipherseed(phrase):
    rotchar = list(allchar)
    seedval = input(phrase)
    random.seed(seedval)
    random.shuffle(rotchar)
    rotchar = ''.join(rotchar)
    print(rotchar)
    return rotchar

#call cipherseed
rotchar = cipherseed("Input any value to generate the cipher seed: ")
allchar=list(allchar)
rotchar=list(rotchar)

#encrypt
userphrase = input("Input your phrase to encrypt: ")
passphrase = ""
for i in userphrase:
    if i in allchar:
        passphrase += rotchar[allchar.index(i)]
    else:
        passphrase += i

print("Here's your encoded text:")
print(passphrase)

#decrypt

passphrase2 = input("Type in your encoded text: ")
userphrase2 = ""

rotchar = ""
rotchar = cipherseed("Input the cipher seed: ")

for i in passphrase2:
    if i in rotchar:
        userphrase2 += allchar[rotchar.index(i)]
    else:
        userphrase2 += i

print("Here's your decoded text")
print(userphrase2)
