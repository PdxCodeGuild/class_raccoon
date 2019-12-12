import random
possibilities = ["rock", "paper", "scissors"]
continue_YN = "y"

while continue_YN == "y":
    user_choice = input("Please choose rock, paper, or scissors: ").lower()
    comp_choice = random.choice(possibilities)
    if user_choice == comp_choice:
        continue_YN = input("Tie, want to try again? Y/N ").lower()
    else:
        if user_choice == possibilities[0]:
            if comp_choice == possibilities[1]:
                print("You lose")
            else:
                print("You win")
        if user_choice == possibilities[1]:
            if comp_choice == possibilities[2]:
                print("You lose")
            else:
                print("You win")
        if user_choice == possibilities[2]:
            if comp_choice == possibilities[0]:
                print("You lose")
            else:
                print("You win")
        continue_YN = input("Want to try again? Y/N ").lower()
else:
    print("Thanks for playing")
