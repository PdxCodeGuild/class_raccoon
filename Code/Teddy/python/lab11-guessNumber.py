# Lab 11: Guess the Number
import random
import time

def com_num(x):
    x = random.randint(1,10)
    return x

#  initial counter
count = 1

play_again = 'y'

while play_again == 'y':
    guess_num = int(input('What is your guessing number?(1-10) '))
    com_num = random.randint(1,10)
    random_num = random.randint(1,10)

    if guess_num == random_num:
        print(f'Your guess number is {guess_num}, Computer random is {random_num}.. You won! you guesses {count} times')
    else:
        if guess_num > random_num:
            print(f'Your guess number is {guess_num}, Computer random is {random_num}.. You loose! too high! you guesses {count} times')
        else:
            print(f'Your guess number is {guess_num}, Computer random is {random_num}.. You loose! too low! you guesses {count} times')

    print()
    # Put time delay
    time.sleep(2)
    print('Now! Computer turn')
    # Put time delay
    time.sleep(2)
    print()

    # Switching to computer
    if com_num == random_num:
        print(f'Computer guess number is {com_num}, Computer random is {random_num}.. You won! you guesses {count} times')
    else:
        if com_num > random_num:
            print(f'Computer guess number is {com_num}, Computer random is {random_num}.. Computer loose! too high! you guesses {count} times')
        else:
            print(f'Computer guess number is {com_num}, Computer random is {random_num}.. Computer loose! too low! you guesses {count} times')

    count += 1

    play_again = input('Do you want to play again?(y/n)').lower()
print('Bye')
print()
