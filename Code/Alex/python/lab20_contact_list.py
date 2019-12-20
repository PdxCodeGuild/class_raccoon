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


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
lines = lines[0:-1]
header_list = lines[0].split(',')

contacts_list = []
contacts = []

for i in range(1, len(lines)):
    contacts_list.append(lines[i].split(','))

for i in range(len(contacts_list)):

    contacts_dict = {}

    for j in range(len(header_list)):

        contacts_dict[header_list[j]] = contacts_list[i][j]

    contacts.append(contacts_dict)

print(contacts)


    #print(lines[i].split(','))
