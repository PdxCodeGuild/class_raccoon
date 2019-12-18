#lab15_rot_ver2.py
import string

allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
print(allchar)

def cipher(num):
    rotchar = allchar[num:] + allchar[0:num]
    print(rotchar)
    return rotchar

while True:
    try:
        numval = int(input("What's the rotation amount in this substitution cipher? "))
        numval = numval % len(allchar) - 1
        break
    except ValueError:
        print("Invalid entry!")

rotchar = cipher(numval)
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
for i in passphrase2:
    if i in rotchar:
        userphrase2 += allchar[rotchar.index(i)]
    else:
        userphrase2 += i

print("Here's your decoded text")
print(userphrase2)
