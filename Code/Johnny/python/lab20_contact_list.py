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
print(contact_info)

# CRUD process // CREATE RETRIEVE UPDATE & DELETE
