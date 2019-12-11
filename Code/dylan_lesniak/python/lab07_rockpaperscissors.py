'''
Filename: lab07_rockpaperscissors.py
Author: Dylan
Purpose: Create Rock, Paper, Scissors game
'''

#mods
import random

#main functions
def play_game():
    #variables
    possible_moves = ["rock","paper","scissors"]
    computer_move = random.choice(possible_moves)
    player_move_hash = {"rock":["scissors","paper"],"scissors":["paper","rock"],"paper":["rock","scissors"]}
    print("Welcome to the Rocking Sound Project. \nHere you can compete at the highest levels of Rock, Paper, Scissors.\n")
    print("Please, enter your move (Rock, Paper, or Scissors)")
    player_move = input_checker(input("> ").lower(),possible_moves)
    print(f"You played: {player_move.capitalize()}")
    print(f"The computer played: {computer_move.capitalize()}")
    if player_move == computer_move:
        print("It's a tie!")
    elif player_move_hash[player_move][0] == computer_move:
        print("You win!")
    else:
        print("You lose :(")

def input_checker(str,moves):
    while True:
        if str in moves:
            return str
        else:
            print("Please enter a valid move. ")
            str = input("> ").lower()


cont = "y"
while cont.lower() == "y" or cont.lower() == "yes" or cont.lower() == "yea":
    play_game()
    print("\nWould you like to play again? (y/n)")
    cont = input("> ")
