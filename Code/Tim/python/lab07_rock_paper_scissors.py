import random
import os

game_pieces = ["Rock", "Paper", "Scissors"]

os.system('cls')
user = input("\n\nnunununununununununununununununununununununununununuunununununununnunununun\nHello, what is your name?\nnununununununununununununununununununununununununununununununununununununun \n> ")
game_loop = input(f"Nice to meet you, {user}, do you want to play rock, paper, scissors? (y/n)\nnununununununununununununununununununununuunununununununnununununununununun\n> ")

#Gameplay loop
while game_loop == "y":

    #Game input and randomizer
    user_choice = int(input("\nnunununununununununununununununununununununununununuunununununununnunununun\nWhat's your choice? (1) Rock (2) Paper (3) Scissors\nnunununununununununununununununununununununununununuunununununununnunununun\n> "))
    user_choice = game_pieces[user_choice - 1]
    comp_choice = random.choice(game_pieces)

    # Winning and losing statements
    win = f"\nnunununununununununununununununununununununununununuunununununununnunununun\nYou chose {user_choice} and the computer chose {comp_choice}. You win!\nnunununununununununununununununununununununununununuunununununununnunununun\n"
    lose = f"\nnunununununununununununununununununununununununununuunununununununnunununun\nThe computer chose {comp_choice} and you chose {user_choice}. You lose.\nnunununununununununununununununununununununununununuunununununununnunununun\n"

    # Results
    if user_choice == comp_choice:
        print("That's what the computer picked tooooo! It's a tie!!!")
    elif user_choice == "Rock" and comp_choice == "Paper":
        print(lose)
    elif user_choice == "Rock" and comp_choice == "Scissors":
        print(win)
    elif user_choice == "Paper" and comp_choice == "Scissors":
        print(lose)
    elif user_choice == "Paper" and comp_choice == "Rock":
        print(win)
    elif user_choice == "Scissors" and comp_choice == "Rock":
        print(lose)
    elif user_choice == "Scissors" and comp_choice == "Paper":
        print(win)
    game_loop = input("\nnunununununununununununununununununununununununununuunununununununnunununun\nDo you want to play again? (y/n) \nnunununununununununununununununununununununununununuunununununununnunununun\n> ")
else:
    print(f"\nnunununununununununununununununununununununununununuunununununununnunununun\nOkay, have a good day, {user}\nnunununununununununununununununununununununununununuunununununununnunununun\n")
