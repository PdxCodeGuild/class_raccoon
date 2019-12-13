import random
import os
os.system('cls')

#variables
comp_number = random.randint(1,20)
count = 1
print(comp_number)
user_guess = int(input("\n***********************************************\nGuess a number between 1-20. You have 3 tries.\n***********************************************\n> "))
user_guess_old = user_guess

#loopy loops
while user_guess != comp_number and count < 3:
    if user_guess > comp_number:
        user_guess_old = user_guess
        user_guess = int(input("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nYour guess was too high. Guess again.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n> "))
        count += 1
    elif user_guess < comp_number:
        user_guess_old = user_guess
        user_guess = int(input("\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\nYour guess was too low. Guess again.\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n> "))
        count += 1
    if count >= 2:
        if user_guess == comp_number:
            print("\n***********************************************\nYou guessed correctly!\n***********************************************\n")
            break
        elif abs(user_guess - comp_number) > abs(user_guess_old - comp_number):
            print("Your last guess was closer.")
        elif abs(user_guess - comp_number) < abs(user_guess_old - comp_number):
            print("You're getting closer!")

while count == 3 and comp_number != user_guess:
    print("You LOSE! ")
    break

# while comp_number == user_guess:
#     print("\n***********************************************\nYou guessed correctly!")
#     break
