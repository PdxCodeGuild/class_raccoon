
import random


rps = ['rock', 'paper', 'scissors']
computer_choice = random.choice(rps)
human_choice = input('Choose rock, paper, or scissors: ')

print(f'human chose {human_choice} and computer chose {computer_choice}')


computer_choice = rps.index(computer_choice)
human_choice = rps.index(human_choice)

# 1 beats 0
# 2 beats 1
# 0 beats 2

if human_choice == computer_choice:
    print('tie')
elif human_choice == (computer_choice + 1)%3:
    print('human won')
else:
    print('computer won')

# if computer_choice == human_choice:
#     print('tie')
# elif computer_choice == 0 and human_choice == 1:
#     print('human won')


# rock = 'rock'
# paper = 'paper'
# scissors = 'scissors'
# if computer_choice == human_choice:
#     print('tie!')
# elif computer_choice == rock and human_choice == scissors:
#     print('computer won')
# elif computer_choice == rps[0] and human_choice == rps[2]:
