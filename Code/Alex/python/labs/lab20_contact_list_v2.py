'''*not complete*
Lab 20: Contact List

Version 2

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.

Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''

import string
import re
import os

with open('contacts.csv', 'r') as file:
    lines = file.read().lower().split('\n')
#given to us. this info takes from file. reads it and splits it in lines.

lines = lines[0:-1]#accounting for all lines.
header_list = lines[0].split(',')#the first lines is the headers list. when split by comas
contacts_list = []
contacts = []
# print(lines)


#this turns each line into its own list, splits our list by it's commas and then adds each line to a new list (contacts_list) so that we can then use it in our dictionary
for i in range(1, len(lines)):#range starting at 1 because line 1 is where the header list starts
    contacts_list.append(lines[i].split(','))
#print(contacts_list)

for i in range(len(contacts_list)):#now we use our contacts_list info to create a dictionary
    contacts_dict = {}
    for j in range(len(header_list)):
        contacts_dict[header_list[j]] = contacts_list[i][j]#assigning the value contacts_list[i][j] to the key contacts_dict[header_list[j]
    contacts.append(contacts_dict) #this is appending the dictionary to the contacts list. making a list of dictionaries
while True:
    os.system("clear")
    user_choice = input("Would you like to create, retrieve, update or delete a record?\nYou can also save or quit the session by typing 'save' or 'quit'.\n\n").lower()
#create
    if user_choice == "create":
        new_contact = {}
    #name
        while True:
            flag = ''
            name_choice = input("Name: ").lower()
            for i in name_choice:
                if i in string.ascii_lowercase:
                    continue
                else:
                    flag = "flag"
            if flag == "flag":
                print("invalid input\n")
                continue
            break
        new_contact["name"] = name_choice
    #age
        while True:
            flag = ''
            age_choice = input("Age: ").lower()
            for i in age_choice:
                if i in string.digits:
                    continue
                else:
                    flag = "flag"
            if flag == "flag":
                print("invalid input\n")
                continue
            break
    #email
        email_choice = input("Email: ").lower()

    #color
        while True:
            flag = ''
            color_choice = input("Favorite Color: ").lower()
            for i in color_choice:
                if i in string.ascii_lowercase:
                    continue
                else:
                    flag = "flag"
            if flag == "flag":
                print("invalid input\n")
                continue
            break
    #are you sure
        create_sure = input("Are you sure you want to create this contact? ").lower()

        if create_sure == "yes" or create_sure == "y":
            print("The record was successfully created.\n\n\n")
            contacts.append(new_contact)

        elif create_sure == "no" or create_sure == "n":
            print("The record was not created\n\n\n")
            continue


#retrieve
    elif user_choice == "retrieve":
        retrieve_contact = input("What's the name of the contact you are looking for? ").lower()

        for contact in contacts:
            if retrieve_contact == contact["name"]:
                print(f'\n{contact}')

#update
    elif user_choice == "update":
        update_contact = input("Who's account are we updating? ").lower()

        for contact in contacts:
            if retrieve_contact == contact["name"]:
                input("")

        update_sure = input("Are you sure you want to update this account? ").lower()
        update_approved = print()








    elif user_choice == "delete":
        delete_contact = input("Who's account are we deleting?").lower()
        delete_sure = input("Are you sure you want to delete this account? ").lower()
        delete_really_sure = input("Are you reeeaally sure you want to delete it? ").lower()
        delete_approved = print()

#make a temp list?



    #
    #
    #
    # elif user_choice == "save":
    #
    #
    #
    #
    #
    #
    # elif user_choice == "quit":
    #
    #
    #
    #
    #
    #
    # else:
    #     print("invalid entry" + user_choice)
    input('')
