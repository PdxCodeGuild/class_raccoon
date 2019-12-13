"""
Lab 11: Guess the Number

Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered

random.randint
REPL: read-evaluate-print loop
input, print

Version 4 (optional)

Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).
"""


print("\n\n\n\n\n\n\n\nWelcome to the Guess the Number game!\n\n")


import random

computer_choice = random.randint(1,10)#might need to be 11
computer_choice = int(computer_choice)
computer_choice = abs(computer_choice)


user_guess = input("Guess a number ")
user_guess = int(user_guess)
user_guess = abs(user_guess)

guess_again = user_guess
guess_again = int(guess_again)
guess_again = abs(guess_again)


hot_cold = (user_guess - computer_choice)#abs because the difference could be negative depending on what they pick
hot_cold1 = hot_cold


counter = 0
while guess_again != "done":

    user_guess = input("Just kidding. This is where you guess a number ")
    user_guess = int(user_guess)
    user_guess = abs(user_guess)

    hot_cold = (user_guess - computer_choice)#abs because the difference could be negative depending on what they pick

    counter += 1

#    if int(user_guess) > computer_choice:
#        print("\nToo high!")
#    if int(user_guess) < computer_choice:
#        print("\nToo low.")

    if hot_cold1 < hot_cold:
        print("You're getting warmer")

    if int(user_guess) != computer_choice:
        print("\ntry again!\n\n")

    if int(user_guess) == computer_choice:
        print("\nYou guessed my number! Good job\n\n")
        print(f"How many tries it took you to guess my number: {counter}\n\n")
        if counter == 4:
            print("Not bad\n\n\n")
        if counter == 3:
            print("Not bad\n\n\n")
        if counter == 2:
            print("Not bad\n\n\n")
        if counter == 1:
            print("Perfect!\n\n\n")
        if counter > 4:
            print("I think you can do better..\n\n\n")

    guess_again = input("Would you like to continue? If no, type 'done' to quit. ")

    hot_cold1 = hot_cold
