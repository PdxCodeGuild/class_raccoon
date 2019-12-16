# Black jack program, Brandon G. 
#Import
import operator
import random

#Stored variables
cards = {"A":1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q":10, "K": 10}
cont_list = ["Yes", "yes", "continue"]

#Functions for calculating whether to hit or to stay.
def hit_stay(card_1,card_2,card_3):
    x = cards[card_1]
    y = cards[card_2]
    z = cards[card_3]
    
    
    card_total = x + y + z
    # if card_total < 11:
    #     cards[A] = 11
    # else:
    #     cards[A] = 1
        
    if card_total < 21 and card_total > 17:
        return("You should stay.")
    elif card_total < 17:
        return("You should hit.")
    else:
        return("Busted")

#Main Program
while True:
    user_card = input("What cards do you have? ie. '3' space '2' space 'k'.\n:").upper()
    user_card = user_card.split(' ')

    card_1 = user_card[0]
    card_2 = user_card[1]
    card_3 = user_card[2]
    
    
    print(hit_stay(card_1,card_2,card_3))
    again = input("Do you want to play again?")
    if again in cont_list:
        continue
    else:
        print("Goodbye")
        break

