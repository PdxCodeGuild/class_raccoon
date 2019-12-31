'''
Filename: lab20_contact_list.py
Author: Dylan
Purpose: Take in a csv, make various edits, and then edit the file (a backup in this case)
'''
#mods
import helper 

with open('contacts.csv', 'r') as f:
    contents = f.read()

lines = contents.split('\n')
lines = [line for line in lines if line != ""]


def get_headers():
    headers = []
    profile = {}
    headers = lines[0].split(",")
    for header in headers:
        profile[header.capitalize()] = ""
    return headers, profile


def get_contact_dict(lines):
    contacts = [] #this will become a list of dicts, where each dict is one person's record. 
    valid_inputs = lines[1:] #first line is headers, everything after is data. 
    for contact in valid_inputs: #gives us each user.
        contact_split = contact.split(",") #in the csv, all the data is separated by only a comma
        temp_profile = {}
        i = 0
        for attribute in contact_split: #gives us the user information after they've been established in the dict. 
            temp_profile[headers[i].capitalize()] = attribute.capitalize()
            i += 1
        contacts.append(temp_profile)
    return contacts
            
def create_record(): 
    info_list = []
    for i in range(len(headers)):
        print(f"Please enter a new {headers[i].capitalize()}: ")
        info = input("> ").capitalize()
        info_list.append(info)
    temp_profile = {}
    i = 0   
    for attribute in info_list: #gives us the user information after they've been established in the dict. 
        temp_profile[headers[i].capitalize()] = attribute.capitalize()
        i += 1
    contacts.append(temp_profile) #once a dictionary for the new user has been made, it gets thrown into contacts
    print(f"A new record has been created for {info_list[0].capitalize()}. \n")
    

def retrieve_record():
    print("Please enter name of record you would like to retrieve. ")        
    name = name_checker(input("> ")).capitalize()
    record = [record for record in contacts if record["Name"] == name] #gives back the record if the "Name" key matches.
    print(f"Here is the record for {name}. \n{record[0]}\n")

def update_record():
    print("Whose record would you like to update? ")
    name = name_checker(input("> ")).capitalize()
    record_idx = find_record_idx_by("Name", name)
    print("What attribute would you like to update? ")
    attribute = attribute_checker(input("> ")).capitalize()
    print("Please enter update: ")
    update = helper.text_checker(input("> ")).capitalize()
    contacts[record_idx][attribute] = update #using the record_idx, we find the proper record w/in list of dictionaries. 
    print(f"{name}'s {attribute} has been updated. ")
    print(f"{contacts} \n")

def find_record_idx_by(attribute, value):
    record_idx = 0
    i = 0 
    for record in contacts:
        if record[attribute] == value:
            return i
        i += 1 #I shouldn't have to write in an escape her as one of the checker methods should have handled that already. 

def delete_record():
    print("Who would you like to delete from records? ")
    name = name_checker(input("> ")).capitalize()
    record_idx = find_record_idx_by("Name", name)
    del contacts[record_idx]
    print(f"{name} has been deleted. " )
    print(f"{contacts} \n")

def name_checker(name):
    all_names = []
    for record in contacts:
        for attribute in record:
            if attribute == "Name":
                all_names.append(record[attribute])
    return helper.text_checker(name, all_names)

def attribute_checker(attribute):
    attribute = helper.text_checker(attribute, headers)
    attribute_idx = [i for i in range(len(headers)) if attribute in headers[i]]
    return headers[attribute_idx[0]]

def create_csv():
    new_str = ""
    for record in contacts:
        record_str = ""
        for keys in record:
            record_str += record[keys] + ","
        record_str = record_str[:-1] + "\n"
        new_str += record_str
    return new_str

def crud(): 
    create_record()
    retrieve_record()
    update_record()
    delete_record()


if __name__ == "__main__":
    headers, profile = get_headers()
    contacts = get_contact_dict(lines)
    crud()
    new_csv = create_csv()

    with open('contacts_backup.csv', 'w') as contacts_backup:
        contacts_backup.write(new_csv)
    
