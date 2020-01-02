


# Implement a CRUD REPL

#     Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
#     Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
#     Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
#     Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
import string


with open('contact.csv', 'r') as file:
    lines = file.read().split('\n')


def save_to(values):
    values = str(values)
    with open('contact.csv', 'w') as file:
        file.write(values).split('\n')


def get_lines(lines):
    new_list = []
    for line in lines:
        new_list.append(line.split(","))
    return new_list

def get_keys(new_list):
    keys = new_list[0]
    return keys  

def get_values(keys, data):
    new_list = data[1:]
    new_contact_list = []
    for i in range(len(new_list)):
        contact_dict = {}
        for j in range(len(keys)):
            contact_dict[keys[j]] = new_list[i][j]
        new_contact_list.append(contact_dict)
        new_contact_list.split(",\n")
    return new_contact_list

def manipulate_contacts(keys,contact):
    update_user = input("Enter your information, separated by a comma. ie. Brandon,33,b@gmail.com,blue.\n:")
    update_user = update_user.split(",")
    contact_dict = {}
    for j in range(len(keys)):
        contact_dict[keys[j]] = update_user[j]
    return contact_dict

def what_to_do():
    contact = get_lines(lines) #gets the contact list from the CSV
    keys = get_keys(contact) #gets the keys from the contact list
    values = get_values(keys, contact) #assigns the values from the list to the new dictionary
    adjust = manipulate_contacts(keys, values)

    to_do = input("Do you want to add, find, update or delete?\n:").lower()
    if to_do == "add":
        adjust = manipulate_contacts(keys, values)
        values.append(adjust)
        save_to(values)
        return(values)
        
    elif to_do == "find":
        who_find = input("Who do you want to find?:")
        for person in values:
            if who_find == person["name"]:
                return(person)
        else:
            return("not in database.")

    # elif to_do == "update":
    #     print(lines)
    #     who_update = input("Who do you want to update?")
    #     for who_update in values:


    # # elif to_do == "delete":

    # else:
    #     print("goodbye")    
#Calls function
print(lines)
print(what_to_do())
# save_to(values)
#create function with while loop that asks if they want add, or find, update or delete.

#create a function that saves to the file using the while open with W. send values function to this function. 





