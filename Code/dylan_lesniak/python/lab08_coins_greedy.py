'''
Filename: lab08_coins_greedy.py
Author: Dylan
Purpose: Choose the most efficient selection of coins for a given cent value
'''

#this method will assume a standard US coin value set 
def get_change(cents):
    coins = [1,5,10,25]
    coin_list = []
    while cents > 0:
        if cents >= coins[-1]:
            coin_list.append(coins[-1])
            cents -= coins[-1]
        else:
            coins = coins[:-1]
    return coin_list

print(get_change(14))

#The shortcomming with this function is that it won't give us the fewest coins possible in every case.