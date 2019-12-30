'''
Lab 20: Contact List
Let's build a program to manage a list of contacts, using a CSV "comma-separated values" file. Create a text file,
paste the following content, and save it as "contacts.csv".

name,age,email,favorite color
joe,34,joe@gmail.com,blue
jane,43,jane@gmail.com,green
jill,65,jill@gmail.com,orange

Using Python open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'joe', 'age': '34', 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age':'43' ...}
]

I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''

# Version 1
import re

# Creats emty dictionary
contact = {}

# Open file
with open('product.csv', 'r') as file:
    # Read file, split btw line and assigned to variable names lines
    lines = file.read().split('\n')

# Put the first line to variable names headers
headers = lines.pop(0).split(',')

print(headers)
print('--------')

# Split the words of each line by , using expression
for i in range(len(lines)):
    lines[i] = re.split(r'[,]+', lines[i])
print(lines)

print('--------')

# Loop each header's key followed by value
for i in range(len(lines)):
    for j in range(len(headers)):
        contact[headers[j]] = lines[i][j]
    print(contact)

print()
