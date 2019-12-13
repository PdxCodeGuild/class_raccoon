#Welcome to the guess the number game
import random


def comparison(y):
    i = 1
    user_guess = input("Go ahead.. Have a guess\n:")
    user_guess = int(user_guess)
    
    # print(npc)
    if user_guess == y:
        print(f"You got it there Mr Jedi.. You guessed my number in {i} tries.")
        exit()
    
def tries_left(i):
     left = 10 - i 
     print(f"You have {left} tries left.")      



print("Welcome to guess the number program. This will be soooo intense.... \nYou will have 5 tries to beat the computer. \nAfter your guess (if incorrect) type yes to guess again or no to exit.")
i = 0
while i <= 9:
    i += 1
    npc = random.randint(0,10)
    comparison(npc)
    remaining = 10 - i 
    print(f"You are at {i} tries. You have {remaining} tries left.")

    print("Type yes to guess again. Or no to give up. You get 10 tries...")
    user_again = input("")
    if user_again == "no":
        print("Have it your way. Goodbye...")
        break
else:
    print("Nice try. You used up all of your tries. Goodbye!!")