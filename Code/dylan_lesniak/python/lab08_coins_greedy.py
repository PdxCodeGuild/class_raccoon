'''
Filename: lab08_coins_greedy.py
Author: Dylan
Purpose: Choose the most efficient selection of coins for a given cent value
'''

#this method will assume a standard US coin value set
def get_change(cents):
    cents = input_checker(cents)
    coins = [1,5,10,25]
    coins_counter = {1:0,5:0,10:0,25:0}
    while cents > 0:
        if cents >= coins[-1]:
            coins_counter[coins[-1]] += 1
            cents -= coins[-1]
        else:
            coins = coins[:-1]
    print(f"You want {coins_counter[1]} penny(ies), {coins_counter[5]} nickel(s), {coins_counter[10]} dime(s), and {coins_counter[25]} quarter(s).")

def input_checker(num):
    while True:
        if num.isdigit():
            return int(num)
        else:
            print("Please make a valid entry")
            num = input("> ")

cont = "y"
while cont == "y":
    print("How many cents would you like change for? Do not enter special characters. ")
    get_change(input("> "))
    print("\nWould you like to enter a new amount? (y/n)")
    cont = input("> ").lower()

#The shortcomming with this function is that it won't give us the fewest coins possible in every case.
