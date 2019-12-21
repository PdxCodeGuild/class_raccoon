'''*not complete*
Lab 20: Contact List

Version 2

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
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


attribute_input = contacts.append(input(""))
