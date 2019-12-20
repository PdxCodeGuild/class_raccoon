'''

'''
#mods
import helper 

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = {
}

def get_contact_dict(lines):
    valid_inputs = lines[1:]
    for contact in valid_inputs:
        contact_split = contact.split(",")
        name = contact_split[0].capitalize()
        age = contact_split[1]
        email = contact_split[2]
        color = contact_split[3]
        person_dict = {"Age": age, "Email": email, "Favorite color": color}
        contacts[name] = person_dict
    
'''
    Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''

def create_record(): 
    print("Please enter a new name: ")
    name = helper.text_checker(input("> ")).capitalize()
    print("Please enter an age for that person. ")
    age = helper.digit_checker(input("> "))
    print("Please enter an email address for that person. ")
    email = input("> ") #write email_checker
    print("Please enter a favorite color.")
    color = helper.text_checker(input("> "))
    contacts[name] = {"Age": age, "Email": email, "Favorite color": color}
    print(f"A new record has been created for {name}. \n")

def retrieve_record():
    print("Please enter name of record you would like to retrieve. ")
    name = helper.text_checker(input("> "), contacts).capitalize()
    print(f"Here is the record for {name}. \n{contacts[name]}\n")

def update_record():
    print("Whose record would you like to update? ")
    name = helper.text_checker(input("> "), contacts).capitalize()
    print("What attribute would you like to update? ")
    attributes = []
    for attribute in contacts[name]:
        attributes.append(attribute)
    update_attribute = helper.text_checker(input("> "), attributes).capitalize()
    print("Please enter update: ")
    update = helper.text_checker(input("> ")).capitalize()
    contacts[name][update_attribute] = update
    print(f"{name}'s {update_attribute} has been updated. \n")

def delete_record():
    print("Who would you like to delete from records? ")
    name = helper.text_checker(input("> "), contacts).capitalize()
    del contacts[name]
    print(f"{name} has been deleted. \n" )



def crud(): 
    create_record()
    retrieve_record()
    update_record()
    delete_record()


if __name__ == "__main__":
    get_contact_dict(lines)
    crud()