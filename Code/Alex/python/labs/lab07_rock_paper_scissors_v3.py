'''*not complete*
Lab 7: Rock Paper Scissors

Version 3 (optional)

Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''



#i imported the random module to enable the computer to play back using a random choice of the given strings
import random

move_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
#possible choices listed as seperate strings within a variable
#for v2 i selected a variable for the user if they chose to play the game again. In order to start the while loop again.
play_again = "y"
while play_again == "y":

    user_move_choice = input(f"\n\nrock, paper, scissors, lizard, spock GO\n\n\n\n\n\n\n\n\n                                   ")
    #I utilized the variable above to give the user choices to choose from and then input into the calculation.

    computer_move_choice = random.choice(move_list)#this is the computer's calculation for it's choice. Again I utilized the variable representing the valid choices in order to play.

    if computer_move_choice == move_list[0]: #computer chooses 'rock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\n\nQuit copying me.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\n\nYou've won this round..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\n\nHah! I'm better than you!\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\n\nI crushed your lizard with a rock. I win.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\n\nWhat? Spock vaporized my rock! I guess you win..\n")

    elif computer_move_choice == move_list[1]: #computer chooses 'paper'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\n\nSorry Charlie.\nI win.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\n\nQuit copying me.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\n\nAlright, i give up.. you win\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\n\nWhat the heck! Your lizard ate my paper man... you win\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\n\nPaper disproves Spock. \nYou loose.\n")

    elif computer_move_choice == move_list[2]: #computer chooses 'scissors'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\n\nYou win.\nI loose.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\n\nI win.\nYou loose.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\n\nquit copying me.\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\n\nI decapitated your lizard with my scissors.\nYou loose.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\n\nSpock smashes scissors. \nYou win.\n")

    elif computer_move_choice == move_list[3]: #computer chooses 'lizard'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\n\nyou win. rock smashed lizard\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\n\nLizard ate your piece of paper.\nI win.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\n\nscissors decapitated lizard..\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\n\ntied.            but my lizard is cooler than yours.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\n\nlizard poisons spock.\n\n                                     You loose.\n")

    elif computer_move_choice == move_list[4]: #computer chooses 'spock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\n\nspock vaporizes rock.\n I win!\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\n\nyou win. paper disproves spock\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\n\nspock smashes scissors.\n     Ya lost.\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\n\ni guess you win\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\n\nIt's a tie.\n\n\n\n\n\n\n                       Spock... \n\n\n              meet Spock.\n")

        #v2 addition. i used the user input to ask if they wanted to play again and then created a while loop incase of invalid entry
    play_again = input("play again? y/n\n\n").lower()

        #I kept it inside the original while loop in order to give them the option of whether or not they wanted to leave the game.
    while play_again != "n" and play_again != "y":
        print(f"\nWrong.")

        play_again = input("\nWould you like to play again? y/n\n").lower()

        if play_again == "n":
            break

#ending while loop
else:
    print("\nokay bye\n╭∩╮(ツ)_/¯\n")#classraccoon
