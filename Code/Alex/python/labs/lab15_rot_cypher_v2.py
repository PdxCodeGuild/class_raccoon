'''
Version 2 (optional)

Allow the user to input the amount of rotation used in the encryption / decryption.
'''

import string
#i imported the string to save some typing

alphabet = string.ascii_lowercase #this is our reference of organized letters
user_string = input("Yo. gimme a string of letters and i will encode it ROT13 style  ")#this is the mash of letters we need to organize and alter

#with this version we give them a choice of how many times to encrypt. has to be an int
user_encrypt_choice = int(input("How many rotations do you want to encrypt each letter with? "))

password = ''# we did this because we are dealing with strings and we need to define what the new password will be

for i in range(len(user_string)):#for each indicy in the range of the length of the users mashed input of letters
    index_i = alphabet.find(user_string[i])#now we define the index of the user's letter "user_string[i]" by finding it in the alphabet of letters(our main reference)

    index_i += user_encrypt_choice#amount of rotation per letter
    password += alphabet[index_i%26]#now we take the letter which can be past index 26 of the alphabet and we mod it through the list of letters again and again to give us a letter every time.

print(password)#the new letters
