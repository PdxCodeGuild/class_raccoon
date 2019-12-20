'''
Lab 20: Contact List

Let's build a program to manage a list of contacts, using a CSV "comma-separated values" file. Create a text file, paste the following content, and save it as "contacts.csv".

name,age,email,favorite color
joe,34,joe@gmail.com,blue
jane,43,jane@gmail.com,green
jill,65,jill@gmail.com,orange
Using Python open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'joe', 'age': '34', 'email': 'joe@gmail.com', 'favorite color':'blue'},
    {'name':'jane', 'age':'43' ...}
]
'''
