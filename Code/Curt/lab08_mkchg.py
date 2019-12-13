#lab08_mkchg.py

print("Let's convert some money!")

#optional version 3
coins = [
    ('quarter(s)', 25),
    ('dime(s)', 10),
    ('nickel(s)', 5),
    ('penny/pennies', 1)
]

#Version 1 - Pennies
user_in = ""
while isinstance(user_in, int) == False:
    user_in = input("How much money do you have (in pennies)? ")
    if user_in.isdigit() == True:
        user_in = int(user_in)

print("You have:")
for coin in coins:
    name, num = coin
    count = user_in//num
    print(f"{count} {name}")
    user_in = user_in - num * count

#Version 2 - In dollars:
user_in = ""
while isinstance(user_in, float) == False:
    user_in = input("How much money do you have (in dollars)? ")
    try:
        user_in = float(user_in) * 100
    except ValueError:
        print("Invalid entry!")

print("You have:")
for coin in coins:
    name, num = coin
    count = int(user_in//num)
    print(f"{count} {name}")
    user_in = user_in - num * count
