'''
Filename: lab11_num_guess.py
Author: Dylan 
Purpose: Game where user must guess computer number, or computer must guess user number(feature to-be-added)
'''

#mods 
import random

#functions
def user_or_pc():
    print("""Welcome to the Guessing Game!
Would you like to guess the number, or should the pc guess yours? (I/PC)""")
    player = user_checker(input("> "))
    if player == "I":
        player_guesser()
    else:
        pc_guesser()


def user_checker(str):
    while True:
        correct_str = []
        for letter in str:
            if letter.isalpha():
                correct_str.append(letter)
        correct_str = "".join(correct_str).upper()
        if correct_str == "I" or correct_str == "PC":
            return correct_str
        else:
            print("Please choose valid entry. Either \"I\" or \"PC\".")
            str = input("> ")
    
def player_guesser():
    print("The computer will guess a number between 1 and 10. No more. No less.")
    computer_num = random.randint(1,10)
    cont_game = 'y'
    user_guesses = []
    incorrect_guesses = 0
    while cont_game == 'y':
        print("Please enter your guess. (1-10)")
        user_guess = digit_checker(input("> "))
        user_guesses.append(user_guess)

        if user_guess == computer_num:
            print("Congrats! You won!")
            input("Click ENTER to continue.")
            cont_game = "escape, dear lord run!!!"
            return
        elif user_guess > computer_num:
            print("Too high. Try again!")
            incorrect_guesses += 1
            print(f"You have made {incorrect_guesses} incorrect guesses.\n")
            guess_compare(user_guesses,computer_num)
        elif user_guess < computer_num:
            print("Too low. Try again!")
            incorrect_guesses += 1
            print(f"You have made {incorrect_guesses} incorrect guesses.")
            guess_compare(user_guesses,computer_num)
        else:
            print("OH NO HOW DID YOU GET HERE OH YOU SUCK YOU BROKE EVERYTHING")
        
def guess_compare(user_guesses,computer_num):
    if len(user_guesses) < 2: 
        return 
    last_guess_diff = abs(user_guesses[-1] - computer_num)
    scnd_to_last_guess_diff = abs(user_guesses[-2] - computer_num)
    if last_guess_diff > scnd_to_last_guess_diff:
        print("Your last guess was closer.")
    elif last_guess_diff < scnd_to_last_guess_diff:
        print("You're getting closer.")
    else:
        print("NOW HOW'D YOU GET HERE STOP BREAKING THINGS!!! ...I work so hard...")

def pc_guesser():
    print("Ok, gonna make the computer do all the work. Noted...")
    print("Please enter a number between 1 and 10.")
    user_num = digit_checker(input("> "))
    incorrect_guesses = 0 
    cont = "y"
    computer_guess_list = random.sample(range(1,11),10)
    i = 0 
    while cont == "y":
        computer_guess = computer_guess_list[i]
        if computer_guess == user_num:
            print(f"The computer has guessed {user_num}! What are the odds?")
            return
        else:
            print(f"Your number is: {user_num}.")
            print(f"The computer guessed: {computer_guess}.")
            esc = input("Click ENTER to let the computer try again, or write 'Done' to exit.\n")
            if esc.capitalize() == "Done":
                cont = "n"
        i += 1

def digit_checker(num):
    while True:
        if num == "3.6":
            print("Not great, not terrible.")
            print("Please enter another integer.")
            num = input("> ")
        elif num.isdigit() and int(num) >= 1 and int(num) <= 10:
            return int(num)
        else:
            print("Please enter valid integer (1-10)")
            num = input("> ")

cont = 'y'
while cont == 'y':
    user_or_pc()
    print("Would you like to play again? (y/n)")
    cont = input("> ").lower()

print("Thanks for playing!")