import os
import string

#print(os.system('dir'))

contact_list = []
contacts = []
crud_choice = input('Would you like to (C) Create, (R) Retrieve, (U) Upadate, or (D) Delete a record? \n> ')


# open file and break into a list of lists separated by lines
with open('contact_lab.csv', 'r') as file:
    lines = file.read().split('\n')
# lines variable has the file separated into individual lines

def dictionary_maker(x):
    for i in range(len(x)):
        contact_list.append(x[i].split(','))
    return contact_list
# contact_list variable is data separating with commas

# creating list of dictionaries
def make_keys(x):
    keys = x[0]
    for i in range(1, len(x)):
        contact_dict = {}
        for j in range(len(keys)):
            # print(keys[j])
            contact_dict[keys[j]] = x[i][j]
        contacts.append(contact_dict)
    return contacts
# contacts var is a list of dictionaries, each with one contact's data

def save_updates(x):
    print(contacts)


dictionary_maker(lines)
make_keys(contact_list)

#Create logic
if crud_choice.lower() == 'c':
    name = input('What is the name of the person you would like to add?\n> ')
    age = input('What is the person\'s age?\n> ')
    email = input('What is their email address?\n> ')
    fav_color = input('What is their favorite color?\n> ')
    conta

# Retrieve logic
elif crud_choice.lower() == 'r':
    retrieve_contact = input('Which contact would you like to retrieve?\n> ')
    # logic to search the list of dictionaries for the value of key 'name'
    for dict in contacts:
        if dict['name'] == retrieve_contact:
            print(dict)

# Update logic
elif crud_choice.lower() == 'u':
    update = input('Which contact would you like to update?\n> ')
    name = input('What is the name of the person you would like to update?\n> ')
    age = input('What is the person\'s age?\n> ')
    email = input('What is their email address?\n> ')
    fav_color = input('What is their favorite color?\n> ')
    for dict in contacts:
        if dict['name'] == update:
            dict['name'] = name
            dict['age'] = age
            dict['email'] = email
            dict['favorite color'] = fav_color
# then use the save updates function to save progress
            save_updates(contacts)


elif crud_choice.lower() == 'd':
    del_choice = input('Which contact would you like to delete?\n> ')
    for dict in contacts:
        if dict['name'] == del_choice:
            contacts.pop(dict)

elif crud_choice.lower() == 'p':
    print(contacts)

# print(contacts)
