#Rock paper scissors game
import random

#Variables
throws = ["Rock", "Paper", "Scissors"]

#Dictionary ---- key-value
choices = {
"1": "Rock",
"2": "Paper",
"3": "Scissors"
}


def results():
    npc = random.choice(throws)
    if choices[user_choice] == npc:
        return("Its a tie!")    
    elif user_choice == "1":
        if npc == "Paper":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You lose. Paper suffocates the rock.")
        elif npc == "Scissors":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You smashed the crap out of the scissors..")
    elif user_choice == "2":
        if npc == "Rock":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You win, paper suffocates the rock.")
        elif npc == "Scissors":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You lose. You just been cut.")
    elif user_choice == "3":
        if npc == "Paper":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You win! Paper didnt stand a chance.")
            return("You win! Paper didnt stand a chance.")
        elif npc == "Rock":
            return(f"You chose {choices[user_choice]} and the computer chose {npc}. You done got smashed.")
            return("You dont got smashed.")



while True:
    print("Welcome to RPS Modified.. Make your selection by chosen the respective number listed below.")
    print("Rock-1\nPaper-2\nScissors-3")
    user_choice = input(": ")

    print(results())
    play_again = input("Play again?: ")

    if play_again == "no":
        print("Goodbye")
        break
