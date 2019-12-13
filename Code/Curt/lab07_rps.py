#lab07_rps.py
import random
print("Let's play rock, paper, scissors!")

#repeat while loop
again_var = 'yes'
while again_var == 'yes':
    #user chooses
    user_ch = ''
    while (user_ch != 'rock' and user_ch != 'paper' and user_ch != 'scissors'):
        user_ch=input("Choose one: rock, paper, or scissors? ").casefold()

    #computer chooses
    rps_list = ['rock','paper','scissors']
    comp_ch = random.choice(rps_list)

    #who won
    #tie conditional
    if user_ch == comp_ch:
        print(f"{user_ch.capitalize()} vs {comp_ch}. It's a tie!")
    #not a tie
    else:
        #player chooses rock
        if user_ch == 'rock':
            #win
            if comp_ch == 'scissors':
                print("Rock beats scissors! You win!")
            #lose
            else:
                print("Paper beats rock. You lose!")
        #player chooses paper
        if user_ch == 'paper':
            #win
            if comp_ch == 'rock':
                print("Paper beats rock! You win!")
            #lose
            else:
                print("Scissors beats paper. You lose!")
        #player chooses scissors
        if user_ch == 'scissors':
            #win
            if comp_ch == 'paper':
                print("Scissors beats paper! You win!")
            #lose
            else:
                print("Rock beats scissors. You lose!")
    #play again
    again_var = input("Do you want to play again (Yes or no)? ").casefold()
