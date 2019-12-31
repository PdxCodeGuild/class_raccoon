'''*not complete*
Lab 11: Guess the Number

Version 3

Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''


import random

print("\n\n\n\n\n\n\n\nGuess a number between 1 & 10\n\n")

computer_choice = random.randint(1,10)#might need to be 11


user_guess = input("or type 'done' to cancel: ")

counter = 0

while user_guess != "done":

    counter += 1

    if int(user_guess) > computer_choice:
        print("\nToo high!")
    if int(user_guess) < computer_choice:
        print("\nToo low.")

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

    user_guess = input("Play again by guessing a number or type 'done' to quit\n\n")
