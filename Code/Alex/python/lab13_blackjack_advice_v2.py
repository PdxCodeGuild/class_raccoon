'''
Lab 13: Blackjack Advice


Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''


print("\n\n\n\n\n\n\n\n\n\n\nLet's play blackjack.\n\n")
print("Here are the card choices:\n\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")


cards_and_values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}


player_card1 = ''
player_card2 = ''
player_card3 = ''

while player_card1 not in list(cards_and_values.keys()):
    player_card1 = (input("\n\nPick first card. "))
while player_card2 not in list(cards_and_values.keys()):
    player_card2 = (input("\n\nPick second card. "))
while player_card3 not in list(cards_and_values.keys()):
    player_card3 = (input("\n\nPick a final card. "))



player_hand = (cards_and_values[player_card1] + cards_and_values[player_card2] + cards_and_values[player_card3])



if player_hand <= 17:
    print(f"\n{player_hand} Hit")
elif player_hand >= 17 and player_hand < 21:
    print(f"\n{player_hand} Stay")
elif player_hand == 21:
    print(f"\n{player_hand} Blackjack!")
elif player_hand > 21:
    print(f"\n{player_hand} Already Busted")
