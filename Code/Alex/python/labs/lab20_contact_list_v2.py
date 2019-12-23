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
    lines = file.read().lower().split('\n')
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

user_choice = input("\n\n\n\n\n\n\n\n\n\n\nWould you like to create, retrieve, update or delete a record? ").lower()

if user_choice == "create":
    name_choice = input("Name: ").lower()
    age_choice = input("Age: ").lower()
    email_choice = input("Email: ").lower()
    color_choice = input("Favorite Color: ").lower()
    create_sure = input("Are you sure you want to create this contact? ").lower()
    create_approved = print()


elif user_choice == "retrieve":
    retrieve_contact = input("What's the name of the contact you are looking for? ").lower()
    print()


elif user_choice == "update":
    update_contact = input("Who's account are we updating? ").lower()
    update_sure = input("Are you sure you want to update this account? ").lower()
    update_approved = print()


elif user_choice == "delete":
    delete_contact = input("Who's account are we deleting?").lower()
    delete_sure = input("Are you sure you want to delete this account? ").lower()
    delete_really_sure = input("Are you reeeaally sure you want to delete it? ").lower()
    delete_approved = print()

else:
    print("invalid entry" + user_choice)
