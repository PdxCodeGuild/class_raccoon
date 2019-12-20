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
#given to us. this info takes from file. reads it and splits it in lines.

#accounting for all lines.
lines = lines[0:-1]

#the first lines is the headers list. when split by comas
header_list = lines[0].split(',')

#we made blank lists to be defined below
contacts_list = []
contacts = []


for i in range(1, len(lines)):#range starting at 1 because of line one being the header list
    contacts_list.append(lines[i].split(','))#we append all indicies separated by comas into the contacts list.

for i in range(len(contacts_list)):#now we take that list and turn it into a dictionary

    contacts_dict = {}#here's our blank dictionary to be added to.

    for j in range(len(header_list)):#for every indicy in the header_list

        contacts_dict[header_list[j]] = contacts_list[i][j]#assigning the value contacts_list[i][j] to the key contacts_dict[header_list[j]

    contacts.append(contacts_dict) #this is appending the dictionary to the contacts list. making a list of dictionaries

print(contacts)
