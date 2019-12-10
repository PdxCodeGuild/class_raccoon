# Lab 4: Magic 8-Ball

import random

# Print a welcome screen to the user.
print('Welcome to Magic 8 balls')

# Use the random module's random.choice() to choose a prediction.
predictions = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely',
            'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
            'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
            'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
            'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
            'Very doubtful']

# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
question = input('What is your question? ')

# Display the result of the 8-ball.
result = random.choice(predictions)
print(result)

again = input('Play again? (y/n)').lower()

while again == 'y' or again == 'yes':
    # Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
    question = input('What is your question? ')

    # Display the result of the 8-ball.
    result = random.choice(predictions)
    print(result)

    again = input('Play again? (y/n)').lower()

else:
    print('Bye')
