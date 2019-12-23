'''
Lab 8: Make Change

Version 2

Have the user enter a dollar amount (1.36), convert this to the total in pennies.
'''


print("\n\#                                /|")
print("\n\n                             （・⊝・)                                   \n")
print("                         |")
print("                       How many dollaz we talkin?                     \n\n")


#User needs to choose a dollar amount to work with
pennies = float(input("dollar amount: "))#now a float instead of an int. because the user will type a float and i cant give a float to an int.

pennies = int(pennies * 100)#but i can convert it after the fact

quarters = pennies // 25 #because quarters are 25 with no remainder

pennies = pennies % 25 #because we need to use the remainder after quarters are calculated to get the amount in order to calculate the next biggest value, in order to get the fewest amount of coins

dimes = pennies // 10

pennies = pennies % 10

nickles = pennies // 5

pennies = pennies % 5

#calculation printed. shows the user
print(f"\n\n\n\n\n\nThis the fewest amount of coins you can have w dat many cents. hehe\n\nquarters: {quarters}\ndimes: {dimes}\nnickles: {nickles}\npennies: {pennies}\n\nsee ya!\n\n")
