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
'''

#i imported the random module to enable the computer to play back using a random choice of the given strings
import random

#intro statement into rock paper scissors game
print("Let's play rock, paper, scissors!")


#possible choices listed as seperate strings within a variable
move_list = ['rock', 'paper', 'scissors']

#I utilized the variable above to give the user choices to choose from and then input into the calculation.
user_move_choice = input(f"\nChoose {move_list[0]}, {move_list[1]}, or {move_list[-1]} to continue. ")

#this is the computer's calculation for it's choice. Again I utilized the variable representing the valid choices in order to play.
computer_move_choice = random.choice(move_list)

#the game begins with the computers response to the input from the user and lists the choices neatly to be evaluated.
print(f"\nI used {computer_move_choice} and you used {user_move_choice}.\n")


if computer_move_choice == move_list[0]: #computer chooses 'rock'
    if user_move_choice == move_list[0]: #user chooses 'rock'
        print("\nIt's a tie!\n")
    if user_move_choice == move_list[1]: #user chooses 'paper'
        print("\nYou've won this round..\n")
    if user_move_choice == move_list[2]: #user chooses 'scissors'
        print("\nHah! I'm better than you\n")

if computer_move_choice == move_list[1]: #computer chooses 'paper'
    if user_move_choice == move_list[0]: #user chooses 'rock'
        print("\nSorry Charlie\n")
    if user_move_choice == move_list[1]: #user chooses 'paper'
        print("\nSo it's a tie..\n")
    if user_move_choice == move_list[2]: #user chooses 'scissors'
        print("\nAlright, i give up.. you win\n")

if computer_move_choice == move_list[2]: #computer chooses 'scissors'
    if user_move_choice == move_list[0]: #user chooses 'rock'
        print("\nYou win. I loose.\n")
    if user_move_choice == move_list[1]: #user chooses 'paper'
        print("\nI win. You loose.\n")
    if user_move_choice == move_list[2]: #user chooses 'scissors'
        print("\nquit copying me.\n")
