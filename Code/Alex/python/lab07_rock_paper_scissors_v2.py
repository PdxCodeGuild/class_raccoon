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

After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit
'''

import random
move = ['rock', 'paper', 'scissors']
user_move_choice = input(f"Choose a move, {move[0]}, {move[1]}, or {move[-1]} ")
computer_move_choice = random.choice(move)
print(f"I use {computer_move_choice}")
print(f"and you used {user_move_choice}")
if computer_move_choice == move[0]: #computer chooses 'rock'
    if user_move_choice == move[0]: #user chooses 'rock'
        print("It's a tie!")
    if user_move_choice == move[1]: #user chooses 'paper'
        print("You've won this round..")
    if user_move_choice == move[2]: #user chooses 'scissors'
        print("Hah! I'm better than you")

if computer_move_choice == move[1]: #computer chooses 'paper'
    if user_move_choice == move[0]: #user chooses 'rock'
        print("Sorry Charlie")
    if user_move_choice == move[1]: #user chooses 'paper'
        print("..So it's a tie..")
    if user_move_choice == move[2]: #user chooses 'scissors'
        print("Alright, i give up.. you win")

if computer_move_choice == move[2]: #computer chooses 'scissors'
    if user_move_choice == move[0]: #user chooses 'rock'
        print("You win. I loose.")
    if user_move_choice == move[1]: #user chooses 'paper'
        print("I win. You loose. ")
    if user_move_choice == move[2]: #user chooses 'scissors'
        print("quit copying me.")
