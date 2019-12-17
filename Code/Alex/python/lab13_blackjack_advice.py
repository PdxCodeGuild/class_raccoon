'''
Lab 13: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
'''

print("\n\n\n\n\n\n\n\n\n\n\nLet's play blackjack.\n\n")
print("Here are the card choices:\n\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")


values = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10,
}


card1 = ''
card2 = ''
card3 = ''

while card1 not in list(values.keys()):
    card1 = input("\n\nPick first card. ").lower()
while card2 not in list(values.keys()):
    card2 = input("\n\nPick second card. ").lower()
while card3 not in list(values.keys()):
    card3 = input("\n\nPick a final card. ").lower()



hand = (values[card1] + values[card2] + values[card3])



if hand <= 17:
    print(f"\n{hand} Hit")
elif hand >= 17 and hand < 21:
    print(f"\n{hand} Stay")
elif hand == 21:
    print(f"\n{hand} Blackjack!")
elif hand > 21:
    print(f"\n{hand} Already Busted")
