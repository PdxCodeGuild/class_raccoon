'''
Lab 8: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered

conditionals, comparisons
arithmetic
Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2

Have the user enter a dollar amount (1.36), convert this to the total in pennies.

Version 3 (optional)

Instead of hard-coding the coins, store them in a list. This way you can make custom coins.

coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''



#User needs to choose a dollar amount to work with
pennies = float(input("Enter a dollar amount.\n"))#now a float instead of an int. because the user will type a float and i cant give a float to an int.

pennies = int(pennies * 100)#but i can convert it after the fact

quarters = pennies // 25 #because quarters are 25 with no remainder

pennies = pennies % 25 #because we need to use the remainder after quarters are calculated to get the amount in order to calculate the next biggest value, in order to get the fewest amount of coins

dimes = pennies // 10

pennies = pennies % 10

nickles = pennies // 5

pennies = pennies % 5

#calculation printed. shows the user
print(f"\n\nI did you a service.. Kind of like a modern day cash register. Here is the fewest amount of coins you will need in change.\n\nThis many quarters: {quarters}\nThis many dimes: {dimes}\nThis many nickles: {nickles}\nThis many pennies: {pennies}")
