#rot 13 lab
import string

alphabet = string.ascii_lowercase

def encrypt(user_pass):
    encrypted = ""
    for x in (user_pass):
   
        i = alphabet.find(x) + 13
        encrypted +=  alphabet[i % 26]
    return encrypted

        

        




user_pass = (input("Enter a password using letters from the alphabet. ie. 'asiillhg'\n:"))


print(encrypt(user_pass))
