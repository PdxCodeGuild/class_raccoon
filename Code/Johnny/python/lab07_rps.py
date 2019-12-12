# lab07_rps.py
"""
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
"""
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
else:
    print("You Lose.")
