#lab20_clist.py
file_path = r'../contacts.csv'

headers = []
with open(file_path, 'r') as file:
    contacts = file.read().split('\n')
    headers = contacts[0].split(",")
file.close()
# print(contacts)
# print(headers)

contactlist = []
for info in contacts[1:len(contacts)]:
    contdict = {}
    info = info.split(",")
    for x in range(len(headers)):
        contdict[headers[x]] = info[x]
    contactlist.append(contdict)

#Version 2 - CRUD
commandlist = ["c","r","u","d","q"]
def create():
    createlist = []
    while len(createlist) != len(headers):
        createinput = input("Please input the following information, separated by commas:\nName, Age, E-mail Address, Favorite Color: ")
        createlist = [x.strip() for x in createinput.split(",")]
    contdict = {}
    for x in range(len(headers)):
        contdict[headers[x]] = createlist[x]
    contactlist.append(contdict)
    print(f"{createlist} added to contacts.\n")
    input("Press RETURN to continue.")


def retrieve():
    entrycount = 0
    retrieveinput = input("Please type the name of the contact: ").lower()
    for dict in contactlist:
        dict['name'] = dict['name'].lower()
        if retrieveinput in dict['name']:
            entrycount += 1
            print(f"Entry {entrycount}:")
            returnent = list(dict.values())
            returnent = "\n".join(returnent)
            print(returnent + "\n")
    if entrycount == 0:
        print("No such name in contact list!")
    input("Press RETURN to continue.")

def update(headers):
    entrycount = 0
    updateinput = input("Please type the name of the contact you would like to update: ")
    #find the contact
    for dict in contactlist:
        dict['name'] = dict['name'].lower()
        if updateinput in dict['name']:
            entrycount += 1
            returnent = list(dict.values())
            returnent = "\n".join(returnent)
            print(returnent + "\n")
            returnent = list(dict.values())
    if entrycount > 1:
        print("Your request returned too many entries! Please be more specific.")
    elif entrycount == 0:
        print("No such name in contact list!")
    #runs after confirming a single valid entry:
    else:
        print(f"What information would you like to update for {returnent[0]}?")

        #pick what information to update
        datatype = 0
        while datatype < 1 or datatype > 3:
            datatype = input("Select a number:\n1: Age\n2: E-mail address\n3: Favorite color\n")
            try:
                datatype = int(datatype)
            except ValueError:
                datatype = 0
        print(f"{returnent[0]}'s current {headers[datatype]} is: {returnent[datatype]}")
        #input new info
        newinfo = input(f"Please input a new entry for {returnent[0]}'s {headers[datatype]}: ")
        newinfo = newinfo.strip()
        returnent[datatype] = newinfo #updates the info in the list
        updatedinfo = "\n".join(returnent) #this is just for display of the updated info
        #rewrite the dictionary entry
        for dict in contactlist:
            print(dict['name'])
            print(returnent[0])
            if dict['name'] == returnent[0]:
                dict[headers[datatype]] = newinfo
        print(updatedinfo)
    input("Press RETURN to continue.")

def delete(contactlist):
    entrycount = 0
    deleteinput = input("Please type the name of the contact you would like to delete: ")
    #find the contact
    for dict in contactlist:
        dict['name'] = dict['name'].lower()
        if deleteinput in dict['name']:
            entrycount += 1
            returnent = list(dict.values())
            returnent = "\n".join(returnent)
            print(returnent + "\n")
            returnent = list(dict.values())
    if entrycount > 1:
        print("Your request returned too many entries! Please be more specific.")
    elif entrycount == 0:
        print("No such name in contact list!")
    #runs after confirming a single valid entry:
    else:
        confirm = ""
        while confirm != 'y' and confirm != 'n':
            confirm = input(f"Are you sure you want to delete {returnent[0]} (Y or N)? ").casefold()
        if confirm == 'y':
            contactlist = [dict for dict in contactlist if not (dict['name'] == returnent[0])]
            print(f"{returnent[0]} deleted from contacts.")
    input("Press RETURN to continue.")
    return contactlist

#Select CRUD function
userinput = ''
while userinput != "q":
    userinput = ''
    while userinput not in commandlist:
        userinput = input("Which command would you like to to do? \n[C]reate a record\n[R]etrieve a record\n[U]pdate a record\n[D]elete a record\n[Q]uit\n").lower()
    if userinput == 'c':
        create()
    if userinput == 'r':
        retrieve()
    if userinput == 'u':
        update(headers)
    if userinput == 'd':
        contactlist = delete(contactlist)
    #Version 3 - Rewrite CSV (Yes, I cheated by rewriting the whole file)
    newfile = ",".join(headers)
    for dict in contactlist:
        newfile += "\n" + ",".join(dict.values())
    with open(file_path, 'w') as file:
            file.write(newfile)
    file.close()