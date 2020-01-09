#bruteforce.py
import string

allchar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
string.whitespace
print(allchar)

real = input("Input your password: ")
password = ''
for x in allchar:
