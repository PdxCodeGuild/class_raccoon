import string

text = input('Enter your text here\n> ')
rotation = int(input('How many characters would you like to rotate?\n> '))
indexlist = ''


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotify(text):
    password = ''
    for i in range(len(text)):
        indexlist = alphabet.find(text[i]) + rotation
        indexlist %= 26
        password += alphabet[indexlist]
    print(password)
rotify(text)
