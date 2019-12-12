'''
Lab 7: Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
Version 2 (optional)

After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

Version 3 (optional)

Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''



#i imported the random module to enable the computer to play back using a random choice of the given strings
import random

#intro statement into rock paper scissors game
print("It's time to get down with some rock, paper, scissors, lizard, spock.")


#possible choices listed as seperate strings within a variable
move_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#for v2 i selected a variable for the user if they chose to play the game again. In order to start the while loop again.
play_again = "yes"
while play_again == "yes":

#I utilized the variable above to give the user choices to choose from and then input into the calculation.
    user_move_choice = input(f"\nChoose {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[-1]} to continue. ")

#this is the computer's calculation for it's choice. Again I utilized the variable representing the valid choices in order to play.
    computer_move_choice = random.choice(move_list)

#the game begins with the computers response to the input from the user and lists the choices neatly to be evaluated.
    print(f"\nI used {computer_move_choice} and you used {user_move_choice}.\n")


    if computer_move_choice == move_list[0]: #computer chooses 'rock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nIt's a tie!\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nHah! I'm better than you!\n")
        elif user_move_choice == move_list[3]: #user chooses 'paper'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[4]: #user chooses 'scissors'
            print("\nHah! I'm better than you!\n")

    elif computer_move_choice == move_list[1]: #computer chooses 'paper'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nSorry Charlie\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nSo it's a tie..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nAlright, i give up.. you win\n")
        elif user_move_choice == move_list[3]: #user chooses 'paper'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[4]: #user chooses 'scissors'
            print("\nHah! I'm better than you!\n")

    elif computer_move_choice == move_list[2]: #computer chooses 'scissors'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nYou win. I loose.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nI win. You loose.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nquit copying me.\n")
        elif user_move_choice == move_list[3]: #user chooses 'paper'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[4]: #user chooses 'scissors'
            print("\nHah! I'm better than you!\n")

    elif computer_move_choice == move_list[3]: #computer chooses 'lizard'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nSorry Charlie\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nSo it's a tie..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nAlright, i give up.. you win\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nHah! I'm better than you!\n")

    elif computer_move_choice == move_list[4]: #computer chooses 'spock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nYou win. I loose.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nI win. You loose.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nquit copying me.\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nHah! I'm better than you!\n")

#v2 addition. i used the user input to ask if they wanted to play again and then created a while loop incase of invalid entry
    play_again = input("Would you like to play again?\n").lower()

#I kept it inside the original while loop in order to give them the option of whether or not they wanted to leave the game.
    while play_again != "no" and play_again != "yes":
        print(f"\ninvalid input.")

        play_again = input("\nWould you like to play again?\n").lower()

        if play_again == "no":
            break

#ending while loop
else:
    print("\nokay bye\n╭∩╮(ツ)_/¯\n")#classraccoon
