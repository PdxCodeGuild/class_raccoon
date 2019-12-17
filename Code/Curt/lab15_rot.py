#lab15_rot.py
import string

alphabet = string.ascii_lowercase
print(alphabet)

def cipher(num):
    rotalpha = alphabet[num:] + alphabet[0:num]
    print(rotalpha)
    return rotalpha

numval = int(input("What's the rotation amount in this substitution cipher? "))
numval = numval % 26 - 1

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

print(userphrase)
print(passphrase)
