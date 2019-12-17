#lab15_rot.py
import string

alphabet = string.ascii_lowercase
print(alphabet)

def cipher(num):
    rotalpha = alphabet[num:] + alphabet[0:num]
    print(rotalpha)
    return rotalpha

while True:
    try:
        numval = int(input("What's the rotation amount in this substitution cipher? "))
        numval = numval % 26 - 1
        break
    except ValueError:
        print("Invalid entry!")

rotalpha = cipher(numval)
alphabet=list(alphabet)
rotalpha=list(rotalpha)

userphrase = input("Input your phrase to encrypt: ").lower()
passphrase = ""

for i in userphrase:
    if i in alphabet:
        passphrase += rotalpha[alphabet.index(i)]
    else:
        passphrase += i

print("Here's your encoded text:")
print(passphrase)

#decrypt
passphrase2 = input("Type in your encoded text: ")
userphrase2 = ""
for i in passphrase2:
    if i in rotalpha:
        userphrase2 += alphabet[rotalpha.index(i)]
    else:
        userphrase2 += i

print("Here's your decoded text")
print(userphrase2)
