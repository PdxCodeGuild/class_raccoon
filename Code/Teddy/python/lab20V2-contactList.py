'''
Lab 20: Contact List

Version 2
Implement a CRUD REPL
Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update
and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''

'''
def load_contacts(file_path):
    contacts = []

    # Open file
    with open(file_path, 'r') as file:
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
        contact = {}
        for j in range(len(headers)):
            contact[headers[j]] = lines[i][j]
        contacts.append(contact)

    return headers, contacts

headers, contacts = load_contacts('product2.csv')'''

# Version 2
import re

def load_contacts(file_path):
    # Open file
    with open(file_path, 'r') as file:

        # Read file, split btw line and assigned to variable names lines
        lines = file.read().split('\n')
    lines = [line.split(',') for line in lines]
    # Put the first line to variable names headers
    headers = lines.pop(0)
    # print('-' * 80)
    # print(headers)
    # print('-' * 80)
    # creates the empty list of contacts
    contacts = []
    # loop though lines
    for line in lines:
        # creates empty dictionary
        contact = {}
        for i in range(len(headers)):
            contact[headers[i]] = line[i]
        contacts.append(contact)
    return headers, contacts

# function to fine customer information
def find_contact(name, contacts):
    # Loop through contacts
    for contact in contacts:
        # if found name in contact
        if contact['customer_name'] == name:
            # return value to contact
            return contact
    return None

# print customer information function
def print_contact(contact):
    # Loop through contact
    for key in contact:
        # Output
        print(f'{key} : {contact[key]}')

#assigned file onto variable names csv_path
csv_path = 'product2.csv'

headers, contacts = load_contacts(csv_path)

# print(headers)
# print(contacts)

while True:
    # user input options then assign to variable name menu
    menu = input('''
    Type 1 to create a new customer information
    Type 2 to retrieve a customer information
    Type 3 to update a customer information
    Type 4 to list all the customers information
    Type 5 to save
    Type 0 to quit
    : ''').lower()

    # user input by type 1 or create (to create the new contact)
    if menu == '1' or menu == 'create':
        # creates empty dictionary
        contact = {}
        # loop through the headers
        for header in headers:
            # get new customer info of each headers topic and assign in variable names value
            value = input('What is the ' + header + '? ')
            # put each value to contact
            contact[header] = value
        # append contact
        contacts.append(contact)

    # user input by type 2 or retrieve (to retrieve the existing customer info)
    elif menu == '2' or menu == 'retrieve':
        # User input finding customer name then assigned to variable names name
        name = input('What is the customer name that you want to retrieve an information? ')
        # call the function find_contact by passing name, contacts argument
        contact = find_contact(name, contacts)
        # if doesn't have customer name
        if contact is None:
            # Print output message
            print(f'No customer name {name} on file')
        # found a neme
        else:
            # remove contact from contacts
            contacts.remove(contact)
            # Print output message
            print(f'{name} has been deleted')

    # user input by type 3 or update (to update the existing customer info)
    elif menu == '3' or menu == 'update':
        # User input
        name = input('What is the customer name that you want to update? ')
        # call the function find_contact by passing name, contacts argument
        contact = find_contact(name, contacts)
        # if doesn't have customer name
        if contact is None:
            # Print output message
            print(f'No customer name {name} on file')
        # If there is the customer name on file
        else:
            # user input the topic that need to update by choices
            header = input('What field do you want to update? ('+'/'.join(headers)+') ').lower()
            # If input is not on the list
            if header not in contact:
                # Print output message
                print('That is not a valid field name')
            # If input is on the list
            else:
                # input the new information and assign to a variable name value
                value = input('what is the new value for the field? ')
                # replace new information] onto contact
                contact[header] = value

    # user input by type 4 or list (to list the existing customer info)
    elif menu == '4' or menu == 'list':
        # loop through contacts
        for contact in contacts:
            # call function print_contact by passing argument contact
            print_contact(contact)
            print('-' * 40)

    # user input by type 5 or save (to save the customer info)
    elif menu == '5' or menu == 'save':
        output = ','.join(headers) + '\n'
        lines = [','.join([contact[header] for header in headers]) for contact in contacts]
        output += '\n'.join(lines)
        #open the file with write option as file
        with open(csv_path, 'w') as file:
            # write info into file
            file.write(output)

    # user input by type 0 or quit (to quit the program)
    elif menu == '0' or menu == 'quit':
        # Print output message
        print('------> Bye')
        print()
        # Then Quit the program
        break

    # user input not in the options
    else:
        # Print output message
        print('Please input the valid option')
