# Implement a CRUD REPL

#     Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
#     Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
#     Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
#     Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


import string

def get_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
    new_list = []
    for line in lines:
        if line != '':
            new_list.append(line.split(","))
    return new_list

def get_contacts(headers, lines):
    new_contact_list = []
    for i in range(len(lines)):
        contact_dict = {}
        for j in range(len(headers)):
            contact_dict[headers[j]] = lines[i][j]
        new_contact_list.append(contact_dict)
        # new_contact_list.split(",\n")
    return new_contact_list

def add_contacts(keys,contact):
    update_user = input("Enter your information, separated by a comma. ie. Brandon,33,b@gmail.com,blue.\n:")
    update_user = update_user.split(",")
    contact_dict = {}
    for j in range(len(keys)):
        contact_dict[keys[j]] = update_user[j]
    return contact_dict
    
def create_csv(headers,contacts):
    csv_str = ','.join(headers)+"\n"
    for i in range(len(contacts)):
        csv_str += ','.join(list(contacts[i].values()))+ "\n"
    return csv_str
        
        

#This function runs the program.....supposedly....
def what_to_do(to_do, headers, contacts):


    if to_do == "add":
        contacts.append(add_contacts(headers, contacts))
        return contacts

    elif to_do == "find":
        who_find = input("Who do you want to find?\n:").lower()
        for person in contacts:
            if who_find == person["name"]:
                
                return ",".join(list(person.values()))
        else:
            return("not in database.")
    elif to_do == "update":
        who_update = input("Who do you want to update?\n:")
        for person in contacts:
            if who_update == person["name"]:
                chose_key = input("What would you like to update?\n:")
                if chose_key in person.keys():
                    person[chose_key] = input("What do you want to change it to?\n:")
                    return(contacts)
                else:
                    return("Not in database. Please enter a correct name.")
    elif to_do == "delete":
        print(lines)
        who_delete = input("Who do you want to delete?\n:")
        for i in range(len(contacts)):
            if who_delete in contacts[i]["name"]:
                contacts.pop(i)
                return(contacts)
    elif to_do == "save":
        
        save = create_csv(headers,contacts)
        print("hello")
        with open('contact.csv', 'w') as file:
            file.write(save)




lines = get_lines('contact.csv')
headers = lines.pop(0)
contacts = get_contacts(headers, lines)
print(f"The current contacts in the list are {lines}")
while True:
    to_do = input("Do you want to add, find, update or delete save or quit?\n:").lower()
    if to_do == "add" or to_do == "find" or to_do == "update" or to_do == "delete" or to_do == "save":
        print(what_to_do(to_do, headers, contacts))
    elif to_do == "quit":
        print('goodbye')
        break
