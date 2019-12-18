'''
Filename: lab08_makechange.py
Author: Dylan
Purpose: Find change amount with fewest number of coins
'''

#I want to do recursion with this because I remember that you can 
#Good practice
#maybe let's do the other problem so I can focus on this for the rest of the day
#I'm also really out of practice with recursion so this'll be tough
#for this problem, let's say change list is 
#let's assume that the change_list is in ascending order e.g. [1,5,10]
'''
def make_change(cents,change_list):
    if cents < 1:
        return cents

    coins_list = []
    while cents > 0:
        if change_list[-1] <= cents:
            coins_list.append(change_list[-1])
            cents -= change_list[-1]
        else:
            make_change(cents,change_list[:-1])
    
    return coins_list

print(make_change(123,[1,5,10,25]))
'''

import sys 
  
# m is size of coins array (number of different coins) 
def minCoins(coins, m, V): 
  
    # base case 
    if (V == 0): 
        return 
  
    # Initialize result 
    res = sys.maxsize 
      
    # Try every coin that has smaller value than V 
    for i in range(0, m): 
        if (coins[i] <= V): 
            sub_res = minCoins(coins, m, V-coins[i]) 
  
            # Check for INT_MAX to avoid overflow and see if 
            # result can minimized 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1
  
    return res 

coins = [9, 6, 5, 1] 
m = len(coins) 
V = 11
print("Minimum coins required is",minCoins(coins, m, V)) 