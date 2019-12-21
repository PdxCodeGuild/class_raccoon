# lab20_contact_list.py
# extract files from contacts.csv with open, and close
import re
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

# pull contacts from index of list[0]
contact_key = lines[0]
contact_key = contact_key.split(',')

# iteriate through list, splits by commas, and appends to contact info list
contact_info = []
for info in lines[1:len(lines)-1]:
    contact_dict = {}
    info = info.split(',')
    for value in range(len(contact_key)):
        contact_dict[contact_key[value]] = info[value]
    contact_info.append(contact_dict)
    print(contact_key)
# print(contact_info)

# CRUD process // CREATE RETRIEVE UPDATE & DELETE
print('Create a new file.')
create_name = input('Enter a name: ').lower()
create_age = input('Enter age: ').lower()
create_email = input('Email address: ').lower()
create_color = input('Favorite color: ').lower()
print(f'File to create. \nName: {create_name}, Age: {create_age}, Email: {create_email} and Favorite color: {create_color}.')
create_file = {'name': create_name, 'age': create_age}
for create in contact_info:
    create.update({create_file})
print(contact_info)

print(contact_key)
print(contact_info[0]['name']) # pulls from list index 0, and key of 'name' and returns it.
print(contact_info[1]['age']) # pulls from contact index 1 and returns key of age
print(contact_info[2]['name'])
print(*contact_info, sep='\n') # print each element of list on seperate by new line
