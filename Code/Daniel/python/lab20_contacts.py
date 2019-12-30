#turn a CSV file into a dictonary of dictionaries
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')


continue_yn = "yes"

contact_info = []
contacts = lines
headers = contacts[0].split(",")



for info in lines[1:len(lines)]:
    contact_dict = {}
    info = info.split(",")
    for value in range(len(headers)):
        contact_dict[headers[value]] = info[value]
    contact_info.append(contact_dict)


while continue_yn == "yes":
    
    user_choice = input("Would you like to create a new record, retrieve a record, update an existing record, or delete a record? ").lower()
    #C part of CRUD(create new )
    if "create" in user_choice:
        new_entry_dict = {}
        new_entry = [input("Please input name:"), input("age:"), input("email:"),input("favorite color:")]
        for value in range(len(headers)):
            new_entry_dict[headers[value]] = new_entry[value]
        contact_info.append(new_entry_dict)
        print(contact_info)
        #I know there are a lot of continue_yn variables. Whenever I put one outside the individual loops it would run through the loop again and then quit for some reason. I'll fix it better when I actually get the whole thing to work.
        continue_yn = input("would you like to make a change another change? (Yes/No): ")
    
    #retrieve user info by name
    if "retrieve" in user_choice: 
        retriever = input("Please type the name of the person who's data you're requesting: ")
        for dictionaries in contact_info:
            if retriever == dictionaries["name"]:
                return_list = dictionaries
                print(return_list)
                continue_yn = input("would you like to make a change another change? (Yes/No): ")
            elif retriever != dictionaries["name"]:
                print("No such person")
                continue_yn = input("Would you like to check another name?")
                if continue_yn != "yes":
                    break
    #Update user info
    if "update" in user_choice:
        updater = input("Please type the name of the person who's data you would like to change: ")
        for dictionaries in contact_info:
            if updater == dictionaries["name"]:
                return_list = dictionaries
                update_key = input("What would you like to change: ")
                update_variable = input("What would you like to change it to: ")
                return_list[update_key] = update_variable
                print(return_list)
                continue_yn = input("Would you like to make another change? ")
    #Delete a user record
    
    if "delete" in user_choice:
        temp_list = []
        deleter = input("Please type the name of the person who's record you would like to delete: ")
        for i in range(len(contact_info)):
            if deleter != contact_info[i]["name"]:
                temp_list.append(contact_info[i])
            
        contact_info = temp_list
        print(contact_info)

                
        
    

else:
    output = ""
    for header in headers:
        output += header + ","
    output += "\n"
    for dictionaries in contact_info:
        for value in list(dictionaries.values()):
            output += value + ","
        output += "\n"
    print(output)
    
    
    with open("contacts.csv", "w") as file:
        file.write(output)
