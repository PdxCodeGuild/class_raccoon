import random
def compare(user_guess, comp_choice):
    return user_guess - comp_choice

comp_choice = random.randint(1,10)
user_tries = 0
guess_hist = []
while user_tries < 10:
    user_tries += 1
    user_guess = (int(input("Pick a number between 1-10 ")))
    if user_guess == comp_choice:
        print(f"You did it, congratulations, it took you {user_tries} tries")
        break
    elif user_guess >= comp_choice:
       print("Try lower, you were off by", compare(user_guess, comp_choice))
    elif user_guess <= comp_choice:
        print("Try higher, you were off by", compare(user_guess, comp_choice))
else:
    print("You had 10 chances to choose a number between 1 and 10 and somehow managed to take more than 10 guesses, well done bucco.")