'''
Lab 4: Magic 8-Ball

Version 2

Using a while loop, keep asking the user for a question, if they enter 'done', exit
'''


#modules
import random


#variables
choices = ["It is certain" , "It is decidedly so" , "Without a doubt" , "Yes, definitely" , "You may rely on it" , "As i see it yes" , "Most likely" , "Outlook good" , "Yes" , "Signs point to yes" , "Reply hazy, try again" , "Ask again later" , "Better not tell you now" , "Cannot predict now" , "Concentrate and ask again" , "Don't count on it" , "My reply is no" , "My sources say no" , "Outlook not so good" , "Very doubtful"]

#introduction and user input

#looping for user to keep playing.
while True:
    user_question = input("\n\nI am the Magic 8 Ball.\nAsk me a yes or no question or i will make absolutely no sense.\n\n...or just type 'done' to quit.\n\n\n").lower().strip()

    if user_question == 'done':
        break

    print(f"\n\n{random.choice(choices)}\n\n\n\n\n")
