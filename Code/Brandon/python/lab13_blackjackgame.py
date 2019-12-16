# Black jack program, Brandon G. 
#Import
import operator
import random

#Stored variables
cards = {"A":1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q":10, "K": 10}
card_key =[]
cont_list = ["Yes", "yes", "continue"]

#Functions for calculating whether to hit or to stay.
def hit_stay(card_1,card_2):
    x = cards[card_1]
    y = cards[card_2]
    # z = cards[card_3]
    
    
    card_total = x + y
         
    if card_total < 21 and card_total > 17:
        return("You should stay.")
    after_hit = 0
    while after_hit < 17:
        
        user_hit = input("You should hit. Are you going to?\n:")
        if user_hit == "yes":
            user_card3 = random.choice(list(cards.keys()))
            after_hit = cards[user_card3] + x + y
            print(f"The flop is {user_card3}")
            new_card_total = after_hit
            if new_card_total > 17 and new_card_total< 21:
                return("You should stay")
                break
            elif new_card_total > 21:
                return("You busted.")
                break
            
                

    else:
        return("Busted")

#Main Program
while True:
    user_card1 = random.choice(list(cards.keys()))
    user_card2 = random.choice(list(cards.keys()))
    print(f"You were dealt {user_card1} and {user_card2} totaling ({user_card1}+{user_card2})")
    
    hand = []
    hand.append(user_card1)
    hand.append(user_card2)

    card_1 = hand[0]
    card_2 = hand[1]

    
    print(hit_stay(card_1,card_2))
    again = input("Do you want to play again?")
    if again in cont_list:
        continue
    else:
        print("Goodbye")
        break
