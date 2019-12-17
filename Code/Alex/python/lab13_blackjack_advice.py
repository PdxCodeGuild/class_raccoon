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

#intro
input("\n\n\n\n\n\n\n\n\n\n\nLet's play blackjack.\n\n\n")
input("Here are the card choices:\n\n\n A\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n J\n Q\n K\n\n\n")

#i made a dictionary for the values that way i could give a value to each card choice
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
} #key's are on the left and values for the keys are on the right.

#i made empty string values for the three card choices since the input in the while loop will be a string
card1 = ''
card2 = ''
card3 = ''

#i used a while loop to make it to where if the user doesnt pick something in the dictionary, it prompts them to pick the card again. Rather than telling them 'invalid entry' or something.
while card1 not in list(values.keys()):
    card1 = input("\n\nPick first card. ").lower()
while card2 not in list(values.keys()):
    card2 = input("\n\nPick second card. ").lower()
while card3 not in list(values.keys()):
    card3 = input("\n\nPick a final card. ").lower()
#i used .lower() and made the keys all lower that way the user could put in uppercase or lowercase and it wouldnt matter

#i then put the strings together to show the total value of the cards chosen
hand = (values[card1] + values[card2] + values[card3])


#i then put in place the instructions of how the game goes and bottaboom bottabing.. good to go
if hand <= 17:
    print(f"\n{hand} Hit")
elif hand >= 17 and hand < 21:
    print(f"\n{hand} Stay")
elif hand == 21:
    print(f"\n{hand} Blackjack!")
elif hand > 21:
    print(f"\n{hand} Already Busted")
