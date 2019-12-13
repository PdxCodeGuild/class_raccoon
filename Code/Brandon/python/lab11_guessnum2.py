#Welcome to the guess the number game
import random


#List to continue or quit. When user presses enter, the game continues. When the user enters a string from continue list, game will exit.
cont_list = ["no", "No", "Nope", "quit", "Quit"]

#Funtions to be called
def comparison(y,i,remaining):
    
    user_guess = input("Go ahead.. Have a guess\n:")
    user_guess = int(user_guess)
    if user_guess == y:
        print(f"You got it there Mr Jedi.. You guessed my number in {i} tries.")
        exit()
    if user_guess != y:
        print(f"You are at {i} tries. You have {remaining} tries left. Maybe try guessing {highlow(user_guess,npc)}.")

def tries_left(i):
    left = 10 - i 
    print(f"You have {left} tries left.")      

def highlow(ug,np):
    if ug < np:
        return("higher")
    elif ug > np:
        return("lower")


print("Welcome to guess the number program. This will be soooo intense.... \nYou will have 5 tries to beat the computer. \nAfter your guess (if incorrect) type yes to guess again or no to exit.")
i = 0
npc = random.randint(1,10)
while i <= 9:
    i += 1
    remaining = 10 - i
    comparison(npc,i,remaining)
     
    # print(f"You are at {i} tries. You have {remaining} tries left. Maybe try guessing{highlow}.")
    again = input("Press enter to continue or type no to end.")
    if again in cont_list:
        print("Goodbye")
        break
    else:
        continue