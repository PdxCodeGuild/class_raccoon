


def load_contacts(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
    lines = [line.split(',') for line in lines]
    # for i in range(len(lines)):
    #     lines[i] = lines[i].split(',')
    headers = lines.pop(0)
    contacts = []
    for line in lines:
        contact = {}
        for i in range(len(headers)):
            contact[headers[i]] = line[i]
        contacts.append(contact)
    return headers, contacts


def find_contact(name, contacts):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

def print_contact(contact):
    for key in contact:
        print(key + ': ' +contact[key])



# fruits = ['apples', 'bananas', 'pears']
# t = fruits[0]
# fruits[0] = fruits[1]
# fruits[1] = t
#
# fruits[0], fruits[1] = fruits[1], fruits[0]


csv_path = 'contacts.csv'

headers, contacts = load_contacts(csv_path)

while True:
    command = input('create, retrieve, update, delete, list, save, or quit? ').lower().strip()
    if command == 'create':
        contact = {}
        for header in headers:
            value = input('what is the contact\'s ' + header + '? ')
            contact[header] = value
        contacts.append(contact)
    elif command == 'retrieve':
        name = input('enter the name of the contact you wish to retrieve: ')
        contact = find_contact(name, contacts)
        if contact is None:
            print('contact not found')
        else:
            contacts.remove(contact)
            print(name + ' has been deleted')
    elif command == 'update':
        name = input('enter the name of the contact you wish to update: ')
        contact = find_contact(name, contacts)
        if contact is None:
            print('contact not found')
        else:
            header = input('what field do you want to update? ('+'/'.join(headers)+') ')
            if header not in contact:
                print('that is not a valid field name')
            else:
                value = input('what is the new value for the field? ')
                contact[header] = value
    elif command == 'list':
        for contact in contacts:
            print_contact(contact)
            print()
    elif command == 'save':
        output = ','.join(headers) + '\n'
        # lines = [','.join(contact.values()) for contact in contacts]
        lines = [','.join([contact[header] for header in headers]) for contact in contacts]
        output += '\n'.join(lines)

        # output = ','.join(headers)
        # for contact in contacts:
        #     for i in range(len(headers)):
        #         output += contact[headers[i]]
        #         if i < len(headers)-1:
        #             output += ','
        #     output += '\n'

        # output = [','.join(headers)]
        # for contact in contacts:
        #     line = []
        #     for header in headers:
        #         line.append(contact[header])
        #     line = ','.join(line)
        #     output.append(line)
        # output = '\n'.join(output)
        # print(output)

        with open(csv_path, 'w') as file:
            file.write(output)

    elif command == 'quit':
        break
    else:
        print('command not recognized')
