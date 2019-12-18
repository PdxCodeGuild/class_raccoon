import string
base_letters = string.ascii_lowercase
rot = 0
while True:
    crypt=input("Do you want to encrypt or decrypt? ").lower()
    if crypt in ["encrypt", "decrypt", "en", "de", "exit"]:
        break
    input("Please enter a valid choice, or exit to exit.")
if crypt in ["encrypt", "en"]:
    while True:
        rot = input("what rotation do you want to encrypt by? ")
        if rot.isdigit():
            break
        input("Please input a valid number.")
    usin = input("Please input the string of letters (numbers and symbols will not be encrypted) that you want to encrypt: ").lower()
    output = []
    for l in usin:
        if l in base_letters:
            leti = base_letters.find(l) + int(rot)
            output.append(base_letters[leti%len(base_letters)])
        else:
            output.append(l)
    stringout = "".join(output)
if crypt in ["decrypt", "de"]:
    while True:
        rot = input("what rotation do you want to decrypt by? ")
        if rot.isdigit():
            break
        input("Please input a valid number.")
    usin = input("Please input the encrypted string: ").lower()
    output = []
    for l in usin:
        if l in base_letters:
            leti = base_letters.find(l) - int(rot)
            output.append(base_letters[leti%len(base_letters)])
        else:
            output.append(l)
    stringout = "".join(output)
print(stringout)
