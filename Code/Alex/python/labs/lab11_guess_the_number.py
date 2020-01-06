'''
Lab 11: Guess the Number

Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered

random.randint
REPL: read-evaluate-print loop
input, print
Version 1

Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)
Below is an example run of the game:

guess the number: 5
try again!
guess the number: 2
try again!
guess the number: 3
correct! you guessed 3 times
'''


import random

print("\n\n\n\n\n\n\n\nLet's play 'Guess the Number'. The computer will guess a random int between 1 and 10. You can then try to guess the number, and the program will tell you whether you are right or wrong.\n\n")

computer_choice = random.randint(1,10)#might need to be 11


user_guess = input("Guess the number or type 'done' to cancel: ")

while user_guess != "done":

    if int(user_guess) == computer_choice:
        print("\nYou guessed my number! Good job\n\n")

    if int(user_guess) != computer_choice:
        print("\ntry again!\n\n")

    user_guess = input("Guess the number or type 'done' to cancel: ")
