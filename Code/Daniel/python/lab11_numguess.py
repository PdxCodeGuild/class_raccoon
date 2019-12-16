import random
def compare(user_guess, comp_choice):
    return abs(user_guess) - abs(comp_choice)
continue_yn = "y"
while continue_yn == "y":
    comp_choice = random.randint(1,10)
    user_tries = 0
    while user_tries < 10:
        user_tries += 1
        user_guess = (int(input("Pick a number between 1-10 ")))
        if user_guess == comp_choice:
            continue_yn = input(f"You did it, congratulations, it took you {user_tries} tries, want to go again? Y/N ").lower()
            break
        elif user_guess >= comp_choice:
            print("Try lower, you were off by", compare(user_guess, comp_choice))
        elif user_guess <= comp_choice:
            print("Try higher, you were off by", compare(user_guess, comp_choice))
    else:
        continue_yn = input("You had 10 chances to choose a number between 1 and 10 and somehow managed to take more than 10 guesses, well done bucco. Want to go again? Y/N ").lower()
else:
    print("Thanks for playing!")