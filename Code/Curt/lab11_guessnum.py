#lab11_guessnum.py
import random

print("Let's play Guess the Number!")
range_num = list(range(1, 11))

def user_input():
    comp_num = random.randint(1, 10)
    pick_num = 0
    while pick_num not in range_num:
        pick_num = input("What is your guess? ")
        try:
            pick_num = int(pick_num)
            if pick_num not in range_num:
                print("Invalid entry!")
            else:
                return (pick_num, comp_num)
        except ValueError:
            print("Invalid entry!")

# #Version 1
# print("I'm thinking of a number between 1 and 10.\nYou get 10 guesses.\nIf it takes you more than 10 guesses to choose between 10 numbers,\nthere's something wrong with you.")
# (pick_num, comp_num) = user_input()
#
# ct_guess = 1
# if pick_num == comp_num:
#     print(f"{comp_num}! Good job! You got it on your first try!")
# else:
#     while pick_num != comp_num and ct_guess < 10:
#         ct_guess = ct_guess + 1
#         pick_num = input("Nope! Try again: ")
#         pick_num = int(pick_num)
#         if pick_num == comp_num:
#             print(f"{comp_num}! That's right! It took you {ct_guess} tries to guess it right.")
#     else:
#         if ct_guess >= 10:
#             print(f"Sorry! It was {comp_num}. You had 10 chances to choose between 10 numbers ¯\\_(ツ)_/¯")
#
# #Version 2 - Unlimited guesses
# print("I'm thinking of another number between 1 and 10. This time you get as many guesses as you want.")
# (pick_num, comp_num) = user_input()
#
# ct_guess = 1
# if pick_num == comp_num:
#     print(f"{comp_num}! Good job! You got it on your first try!")
# else:
#     while pick_num != comp_num:
#         ct_guess = ct_guess + 1
#         pick_num = input("Nope! Try again: ")
#         pick_num = int(pick_num)
#         if pick_num == comp_num:
#             print(f"{comp_num}! That's right! It took you {ct_guess} tries to guess it right.")

#Version 3 - High or low
print("I'm thinking of another number between 1 and 10. This time I'll tell you if you're too high or too low: ")
(pick_num, comp_num) = user_input()

while pick_num != comp_num:
        if pick_num > comp_num:
            pick_num = input("Sorry! Too high! Try again: ")
        else:
            pick_num = input("Sorry! Too low! Try again: ")
        pick_num = int(pick_num)

print(f"{comp_num}! That's right! You win!")

# # Version 4 - Hot or Cold
# print("I'm thinking of another number between 1 and 10.\nGuess as many times as you want.\nI'll tell you if you're getting closer.")
# (pick_num, comp_num) = user_input()
#
# ct_guess = 1
# if pick_num1 == comp_num:
#     print(f"{comp_num}! Good job! You got it on your first try!")
# else:
#     while pick_num1 != comp_num:
#         ct_guess = ct_guess + 1
#         if ct_guess <= 2:
#             pick_num2 = pick_num1 #stores old value as pick_num2
#             pick_num1 = input("Nope! Try again: ")
#             pick_num1 = int(pick_num1)
#             while pick_num1 == pick_num2:
#                 pick_num1 = input("Really? You guessed the same number twice in a row? ")
#                 pick_num1 = int(pick_num1)
#         else:
#             diff1 = abs(comp_num - pick_num1)
#             diff2 = abs(comp_num - pick_num2)
#             if pick_num1 == pick_num2:
#                 while pick_num1 == pick_num2:
#                     pick_num1 = input("Really? You guessed the same number twice in a row? ")
#                     pick_num1 = int(pick_num1)
#             elif diff1 == diff2:
#                 pick_num2 = pick_num1
#                 pick_num1 = input("Not warmer or colder ;-) Try again: ")
#             elif diff1 < diff2:
#                 pick_num2 = pick_num1
#                 pick_num1 = input("Warmer! Try again: ")
#             else:
#                 pick_num2 = pick_num1
#                 pick_num1 = input("Colder! Try again: ")
#
#             pick_num1 = int(pick_num1)
#         if pick_num1 == comp_num:
#             print(f"{comp_num}! That's right! It took you {ct_guess} tries to guess it right.")
#
# #Version 5 - Computer's turn
# import time
# pick_num = 0
# while pick_num not in range_num:
#     pick_num = input("My turn! Pick a number between 1 and 10 and I will try to guess it. I promise I won't peek: ")
#     pick_num = int(pick_num)
#
# guesslist = range_num
# comp_num = random.choice(guesslist)
#
# ct_guess = 1
# if comp_num == pick_num:
#     print(f"{pick_num}! Woo! I got it on my first try!")
# else:
#     while pick_num != comp_num:
#         print(comp_num)
#         time.sleep(.2)
#         guesslist.remove(comp_num)
#         ct_guess = ct_guess + 1
#         comp_num = random.choice(guesslist)
#         if comp_num == pick_num:
#             print(f"{pick_num}! It took me {ct_guess} tries to get it right.")
