'''
Lab 8: Make Change

Version 3

Instead of hard-coding the coins, store them in a list. This way you can make custom coins.
'''


print("\n\n                                /|")
print("\n\n                             （・⊝・)                                   \n")
print("                         |")
print("                       How many dollaz we talkin?                     \n\n")

#list of coins is what we need, in the order that we need them to run through the loop in.
coins = [
    ('quarters\n', 25),
    ('dimes\n', 10),
    ('nickels\n', 5),
    ('pennys\n', 1)
]

#amount is the users input turned into an integer
amount = input('How much?  $')
amount = int(float(amount)*100)

print(f"\n\n\nThis the fewest amount of coins you can have w dat many cents. hehe\n\n")
#calculation
for coin in coins:#runs through each item in the list. in this list the first item is ('quarters', 25)
    num_coins = amount//coin[1]
    #coin[1] is 25

    print(f'{num_coins} {coin[0]}')#coin[0] is 'quarter'
    #num_coins is the amount of quarters from the total amount.

    amount %= coin[1]
    #print(amount)
    # print()
    # amount -= coin[1]*num_coins
