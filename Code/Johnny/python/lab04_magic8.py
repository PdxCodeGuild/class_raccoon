# lab04_magic8.py
"""
Lab 4: Magic 8-Ball

Let's write a program to simulate the classic "Magic Eight Ball"

Concepts Covered

input, print
import
random.choice
Instructions

Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
"""
# import module
import random

#loop
# define answer2 and start while loop
answer2 = 'yes'
while True:
    if answer2 == 'yes':
        # prompt user question
        question_var = input("Welcome! Ask the magic 8 ball question? ").lower()
        print(f"You asked, {question_var}?")

        # answer responses
        answer_var = ["It is certain! ", "It is decidedly so. ", "Yes, definitely! ", "You may rely on it. ", "Outlook good. ", "Yes! ", "Ask again later. ", "Cannot predict now. ", "Don't count on it. ", "Outlook not so good. ", "My sources says no. ", "Very doubtful. ", "My reply is no. "]
        # random choice
        output_var = random.choice(answer_var)
        print(output_var)
# ask while loop question to loop or break 
        answer2 = input("Ask again, or type 'done' to exit. ").lower()
    else:
        break
