#Welcome to the guess the number game
import random


def comparison():
    user_guess = input("Go ahead.. Have a guess\n:")
    user_guess = int(user_guess)
    npc = random.randint(0,10)
    print(npc)
    if user_guess == npc:
        print("You got it there Mr Jedi..")
        exit()
    else:
        comparison()
        print(i)



print("Welcome to guess the number program. This will be soooo intense.... \nYou will have 5 tries to beat the computer. \nAfter your guess (if incorrect) type yes to guess again or no to exit.")
i = 1
while i <= 10:
    i += 1
    comparison()
    print(i)

    print("Guess again? Or give up. You get 10 tries...")
    user_again = input("")
    if user_again == "no":
        print("Have it your way. Goodbye...")
        break
