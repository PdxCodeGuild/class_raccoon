 #--Brewery application. 
#--You can search for breweries in your zip code
#--Select breweries based on type
#--Get the brewery information
#--Link to the website


import requests
import random
import json
import string

def merge(ingredients, measurement): 
      
    merged_list = [] 
    for i in range(min((len(ingredients), len(measurement)))): 
  
        while True: 
            try: 
                tup = (ingredients[i], measurement[i]) 
            except IndexError: 
                if len(ingredients) > len(measurement): 
                    measurement.append('') 
                    tup = (ingredients[i], measurement[i]) 
                elif len(ingredients) < len(measurement): 
                    ingredients.append('') 
                    tup = (ingredients[i], measurement[i]) 
                continue
            # print(tup)
            merged_list.append(tup) 
            
            break
        # print(merged_list)
    for item in (merged_list):  # <-- this unpacks the tuple like a, b = (0, 1)
        if item[0] != None and item[1] != None: 
            print(f"{item[0]}--{item[1]}")

def search_drink_name(user):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={user}"
    response = requests.get(url)
    data = json.loads(response.text)
    drinks = data["drinks"]
    if drinks == None:
        print("That is not going to get you crunk. Are you drunk already?")
        return
    choices = {}
    for drink in drinks:
        ingredients = []
        measurement = []
        mixed = []
        for key in drink:
            if "strIngredient" in key:
                if drink[key] == None:
                    continue
                else:
                    ingredients.append(drink[key])
              
            if "strMeasure" in key:
                if drink[key] == None:
                    continue
                else:
                    measurement.append(drink[key])
        choices[(drink["strDrink"])] = {"ingredients": ingredients, "measurement": measurement, "mixed": mixed, "Instructions": drink["strInstructions"]}
            # merge(ingredients,measurement)
            
    for key in choices:
        print(f"\nThe {key}")
        print(f"\nThe ingredients are :\n<><><><><><><><><><>\n") #{', '.join(choices[key]['ingredients'])} \n")
        merge(ingredients,measurement)
        print('')
        print(f"To make this drink: {choices[key]['Instructions']}\n-------------------------")
    

def search_liqour(user):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={user}"
    response = requests.get(url)
    if response.text == "":
        print("That is not the ingredient you are looking for.... Are you drunk already?")
        return
    data = json.loads(response.text)
    drinks = data["drinks"]

    random.shuffle(drinks)
    counter = 0
    while counter < len(drinks):
        for i in range(counter, counter + 10):
            if i == len(drinks):
                break
            print(f"{i+1}.{drinks[i]['strDrink']}")
        more = input("Enter the number of the drink you want to make or press enter to see 10 more.\n:")
        if more == "":
            counter +=10
        elif more != "":
            if more.isdigit():
                more = int(more)
                if more <= len(drinks):
                    drink_choice = drinks[more-1]
                    search_drink_name(drink_choice["strDrink"])
                else:
                    print("Try another number from the list.")
                    continue
            return
        else:
            break
        
            
        
print("Welcome to the get crunk app. Within this app you will be able to search for drinks by their name, or you can ask me what kind of drinks you can make with the liqour of your choice.\n")

while True:
    what_to_do = input("What would you like to do?\n(1)Search for drink by name.\n(2)Search by liquor or ingredient.\n(3)To Quit.\n")
    if what_to_do == "1":
        user = input("What drink would you like to search for?\n:")
        search_drink_name(user)
    elif what_to_do == "2":
        user = input("What ingredient do you want to use?\n:")
        search_liqour(user)
    elif what_to_do == "3":
        print("Goodbye")
        break
    else:
        print("Invalid entry. Please try again.\n")
    
    