#  Lab 7: Rock Paper Scissors
import random

print('Let\'s Play Rock Paper Scissors')

# variable
choices = ['R', 'P', 'S']


play_again = 'y'

while play_again == 'y':

    # user prompt
    user_choice = input('Rock(r), Paper(p) or Scissors(s)? ').upper()
    # Computer random
    com_random = random.choice(choices)
    print(f'Your guess is {user_choice}. Computer guess is {com_random}')

    # Conditions
    if user_choice == com_random:
        print('Tie')
    else:
        if user_choice == choices[0]:
            if com_random == choices[1]:
                print('You loose!')
            elif com_random == choices[2]:
                print('You win!')
        elif user_choice == choices[1]:
            if com_random == choices[0]:
                print('You win!')
            elif com_random == choices[2]:
                print('You loose!')
        elif user_choice == choices[2]:
            if com_random == choices[0]:
                print('You loose!')
            elif com_random == choices[1]:
                print('You win!')

    play_again = input('Do you want to play again?(y/n)').lower()
else:
    print('Bye')
