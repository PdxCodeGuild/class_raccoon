import os

#print(os.system('dir'))

contact_list = []
contacts = []

with open('contact_lab.csv', 'r') as file:
    lines = file.read().split('\n')
# lines = lines[0:len(lines)-1]

def dictionary_maker(x):
    for i in range(len(x)):
        contact_list.append(x[i].split(','))
    return contact_list

dictionary_maker(lines)

def make_keys(x):
    keys = x[0]
    for i in range(1, len(x)):
        contact_dict = {}
        for j in range(len(keys)):
            # print(keys[j])
            contact_dict[keys[j]] = x[i][j]
        contacts.append(contact_dict)
    return contacts

make_keys(contact_list)
print(contacts)
