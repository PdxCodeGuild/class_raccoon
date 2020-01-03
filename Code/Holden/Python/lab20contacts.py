
with open(r'FFPy\contacts.csv', 'r') as file:
    lines = file.read().split('\n')
keyslist = lines[0].split(",")
contacts = []
for i in range(1, len(lines)):
    datalist = lines[i].split(",")
    print(datalist)
    contactdict = {}
    for j in range(len(keyslist)):
        contactdict[keyslist[j]] = datalist[j]
    contacts.append(contactdict)
print(contacts)
def findentry(Input):
    for i in range(len(contacts)):
        if Input in contacts[i]["name"]:
            return contacts[i]
    return
quit_list = ['quit','q','exit','e','y',"yes"]
while True:
    usin = input("Please choose what you want to do to your contacts(find, add, update, delete, quit):").lower()
    if usin in quit_list:
        break
    print("Your contacts are ", end="")
    if len(contacts) > 0:
        for i in range(len(contacts)):
            if i == len(contacts)-1:
                print(f"and {contacts[i]['name']}.")
                break
            print(f"{contacts[i]['name']}, ", end="")
    else:
        print("empty.")
    if usin == "find":
        found = False
        usin = input("Whose details do you want? ")
        found_entry = findentry(usin)
        print(found_entry)
        continue
    if usin == "add":
        keyiter = 0
        if len(contacts) == 0:
            #do more here
            contactdict["name"] = input("Please input name: ")
            contactdict["email"] = input("Please input email: ")
            contacts.append(contactdict)
        else:
            key = list(contacts[0].keys())
            for i in contacts[0]:
                print(key, keyiter, key[keyiter])
                contactdict[key[keyiter]] = input(f"Please input {key[keyiter]}: ")
                keyiter += 1
            contacts.append(contactdict)
        continue
    if usin == "update":
        current_entry = input("Whose details do you want to update? ")
        found_entry = findentry(current_entry)
        if found_entry != None:
            while True:
                userkey = input("What entry do you want to change/add? ")
                if userkey not in found_entry:
                    for i in range(len(contacts)):
                        contacts[i][userkey] = ""
                found_entry[userkey] = input("Please input the data: ")
                quit_query = input("If you want to quit enter y: ").lower()
                if quit_query in quit_list:
                    break
        continue
    if usin == "delete" or usin == "del":
        current_entry = input("Who do you want to delete? ")
        found_entry = findentry(current_entry)
        if found_entry != None:
            contacts.remove(found_entry)
            print(f"{found_entry['name']} has been removed.")
        else:
            print(f"{current_entry} was already gone. ")
    print(contacts)
no_to_save = ["no","n","quit","q","exit"]
yes_to_save = ["y","yes","save"]
while True:
    save_query = input("Do you want to save the changes to your contacts? ").lower()
    if save_query in no_to_save:
        break
    if save_query in yes_to_save:
        key_out = contacts[0].keys()
        save_output = [",".join(key_out)]
        for contact in contacts:
            lineout = []
            for keys in key_out:
                lineout.append(contact[i][keys])
            save_output.append(",".join(lineout))
        with open(r'FFPy\contacts.csv', 'w') as file:
            file.write('\n'.join(save_output))
        break
    print("Please choose yes or no.")
