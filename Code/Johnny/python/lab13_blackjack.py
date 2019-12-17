# lab13.blackjack.py

# define cards dict
cards_dict = {
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
    'K': 10
}

# input
card1 = input("What is your card? ").upper()
card2 = input("What is your second card? ").upper()
card3 = input("What is your third card? ").upper()
total = cards_dict[card1] + cards_dict[card2] + cards_dict[card3]

# possible outcomes
if total < 17:
    print(f"You have {total}: Hit. ")
elif total >= 17 and total < 21:
    print(f"You have {total}: Stay. ")
elif total == 21:
    print(f"You have {total}: Blackjack! ")
else:
    print(f"You have {total}: Busted. ")
