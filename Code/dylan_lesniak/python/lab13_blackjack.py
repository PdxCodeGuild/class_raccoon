'''
Filename: lab13_blackjack.py
Author: Dylan
Purpose: Give advice for a game of blackjack 
'''

#get three cards from the user.  
#program will just give the user advice on what to do in a real game. 
#can turn into a real game once you've finished lab14

#will return an array of three cards
def get_cards():
    cards = []
    print("Please enter your first card here: ")
    first_card = input_checker(input("> "))
    print("Please enter your second card here: ")
    second_card = input_checker(input("> "))
    print("Please enter your last card here: ")
    third_card = input_checker(input("> "))
    cards = [first_card,second_card,third_card]
    cards.reverse()
    score = get_score(cards)
    advice = get_advice(score)

def get_score(cards):
    score = 0 
    scores_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "J": 10,
        "Q": 10,
        "K":10
    }
    a_count = 0 
    for card in cards:
        if card == "A":
            a_count += 1
        else: 
            score += scores_dict[card]
    while a_count > 0:
        points_to_bust = 21-score
        if points_to_bust > 11:
            score += 11
        elif points_to_bust == 11:
            if a_count == 1:
                score += 11
            else:
                score += 1
        else:
            score += 1
        a_count -= 1
    return score

def get_advice(score):
    print(f"Your score is: {score}")
    if score < 17:
        print("You should hit. \n")
    elif 17 < score < 21:
        print("You should stay. \n")
    else:
        print("You WENT BUST!!! Lol \n")


def input_checker(txt):
    valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
    while True:
        if txt.upper() in valid_inputs:
            return txt.upper()
        else:
            print("Invalid input. Please try again.")
            txt = input("> ")


#enter the while continue loop kinda thing here
print("Welcome to Blackjack! The interactive game!")
cont = 'y'
while cont == 'y':
    print("The possible cards you can play are (1, 2, 3, 4, 5, 6, 7, 8, 9, J, K, Q, A).")
    print("The face cards are worth 10 points except for the Ace which is worth either 11 or 1 if 11 would put you over 21.")
    get_cards()
    print("Would you like to play again?")
    cont = (input("> "))r