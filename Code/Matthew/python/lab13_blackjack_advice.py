



def card_value(card):
    if card == 'a':
        return 1
    elif card in ['j', 'q', 'k']:
        return 10
    return int(card)


card_values = {
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



card1 = None
while card1 not in card_values:
    card1 = input('What is the first card?  ').lower()

card2 = input('What is the second card? ').lower()
card3 = input('What is the third card?  ').lower()

hand_value = card_values[card1] + card_values[card2] + card_values[card3]

if hand_value+10 <= 21 and card1 == 'a':
    hand_value += 10
if hand_value+10 <= 21 and card2 == 'a':
    hand_value += 10
if hand_value+10 <= 21 and card3 == 'a':
    hand_value += 10


print('total: ' + str(hand_value))
if hand_value < 17:
    print('HIT')
elif hand_value < 21:
    print('STAY')
elif hand_value == 21:
    print('BLACKJACK')
else:
    print('BUST')
