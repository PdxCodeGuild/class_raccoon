#lab 09 unit converter
#dictionary

unit_dict = { "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000}

def conversion_1(x,measurement):
    global user_1
    if x == "feet":
        user_1 = measurement * unit_dict["ft"]
        print(f"That is {user_1} meters. Below is your requested conversion.")
    elif x == "mile":
        user_1 = measurement * unit_dict["mi"]
        print(f"That is {user_1} meters. Below is your requested conversion.")
    elif x == "meter":
        user_1 = measurement * unit_dict["m"]
        print(f"That is {user_1} meters. Below is your requested conversion.")
    elif x == "kilometer":
        user_1= measurement * unit_dict["km"]
        print(f"That is {user_1} meters. Below is your requested conversion.")
def conversion2(y):
    if y == "meter":
        print(f"{user_1} meters)
    elif y == "feet":
        user_2 = user_1 // unit_dict["ft"]
        print(f"{user_2} feet")
    elif y == "mile":
        user_2 = user_1 * unit_dict["ft"]
        print(f"{user_2} miles")
    elif y == "kilometer":
        user_2 = user_1 * unit_dict["ft"]
        print(f"{user_2} kilometer")


#Welcome and collect data
#Use info collected to run both functions. conv 1 is the meter conversion, conversion 2 is the output
while True:
    print("Welcome to the unit converter.")
    type_1 = input("What type of unit is your measurement? Please enter correct spelling of unit.\n:")
    measurement = input("Please enter the amount to be converted\n:")
    type_2 = input("What would you like to convert it to?\n:")
    measurement = float(measurement)
    conversion_1(type_1,measurement)
    conversion2(type_2)

    convert_again = input("Would you like to convert again?\n:")

    if convert_again == "no":
        print("Goodbye.....")
        break