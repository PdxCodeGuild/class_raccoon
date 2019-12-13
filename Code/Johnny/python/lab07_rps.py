# lab07_rps.py

# import modules to use
import random

# create list
options = ["rock", "paper", "scissors"]
win = ["rockscissors", "paperrock", "scissorspaper"]
tie = ["rockrock", "paperpaper", "scissorsscissors"]
lose = ["rockpaper", "paperscissors", "scissorsrock"]


print("Let's play game. ")
userpick_var = input("Pick Rock, Paper or Scissors: ").lower()
print(f"You picked: {userpick_var}.")

# assign random pick
compick_var = random.choice(options)
print(f"The computer picked: {compick_var}.")

#combine input
output1 = userpick_var + compick_var

# check to find if var is in list above
if output1 in win:
    print("You Win!")
elif output1 in tie:
    print("Tie.")
elif output1 in lose:
    print("You Lose.")
else:
    print("Invalid choice.")
