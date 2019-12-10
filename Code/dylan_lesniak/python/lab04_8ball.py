'''
Filename: lab04_8ball.py
Author: Dylan
Purpose: Write a program to simulate the classic "Magic Eight Ball"
'''

#mods
import random

#variables
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

#functions
def start():
    print("""Welcome to the Magic World of 8 Ball!
Please ask your question to recieve advice.
Or simply type 'Done' to exit the program.""")
    ques = input("> ")
    if ques.capitalize() == "Done":
        return ques.capitalize()

while True:
    if start() == "Done":
        break
    else:
        print(random.choice(answers),"\n")


print("Thank you for using Magic 8 Ball!")