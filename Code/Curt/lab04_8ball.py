#lab04_8ball.py

import random
print("Welcome to the Magic 8 Ball!\n")
ask_var = input("What is your question? ")
answers_var = ["NOOOOOPE!", "All signs point to maybe.", "Stranger things have happened!", "Yes, definitely.", "Ask me again when I'm not on 'me' time.", "HAHAHAHAHAHAHAHA...no.", "Eh, sure.", "Dude, don't be gross."]
print()
print(random.choice(answers_var))
input("\nPRESS ENTER TO CONTINUE")

ask_var = ""
while ask_var != 'done':
    ask_var = input("\nAsk another question, or type 'done' to exit: ").casefold()
    if ask_var == 'done':
        print("\nGood luck! You're gonna need it!")
    else:
        print()
        print(random.choice(answers_var))
        input("\nPRESS ENTER TO CONTINUE")
