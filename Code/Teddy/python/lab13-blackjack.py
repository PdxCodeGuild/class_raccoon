'''
Lab 13: Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
Then, figure out the point value of each card individually.
Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
Use the following rules to determine the advice:

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
# Setup dictionary
cards = {
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
  'k': 10
}
print('Let\'s play Blackjack')

play_again = 'y'
while play_again == 'y':
    first_card = input('What\'s your first card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)? ').lower()
    second_card = input('What\'s your second card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)? ').lower()
    third_card = input('What\'s your third card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)? ').lower()

    score = cards[first_card] + cards[second_card] + cards[third_card]

    if score < 17:
        print(f'{score} Hit')
    elif score >= 17 and score < 21:
        print(f'{score} Stay')
    elif score > 21:
        print(f'{score} Already Busted')
    else:
        print(f'{score} Blackjack!')
    play_again = input('Do you want to play again (y/n)?').lower()
else:
    print('Bye bye')
