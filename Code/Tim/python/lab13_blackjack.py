import random
import os
import string
os.system('cls')

face_cards = ['J','Q','K', 'j', 'q', 'k']

# Getting the card values
first_card = input('What is your first card?\n> ')
if first_card in face_cards:
    first_card = 10
elif first_card == 'A' or first_card == 'a':
    first_card = 11

second_card = input('What is your second card?\n> ')
if second_card in face_cards:
    second_card = 10
elif second_card == 'A' or second_card == 'a':
    first_card = 11

third_card = input('What is your third card?\n> ')
if third_card in face_cards:
    third_card = 10
elif third_card == 'A' or third_card == 'a':
    third_card = 11

total = int(first_card)+int(second_card)+int(third_card)

if total > 21 and first_card == 11 or second_card == 11 or third_card == 11:
    total = total - 10

os.system('cls')

print(f'\nYour total is {total}\n')

if total == 21:
    print("Blackjack!\n")
elif total >= 17 and total < 21:
    print("You should stay\n")
elif total > 21:
    print("Bust! :-( \n")
else:
    print("You should hit!\n")
