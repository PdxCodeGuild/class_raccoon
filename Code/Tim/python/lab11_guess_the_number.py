import random

comp_number = random.randint(1,20)
count = 1
print(comp_number)
user_guess = int(input("Guess a number between 1-20. You have 3 tries. "))

while user_guess != comp_number and count < 3:
    if user_guess > comp_number:
        user_guess = int(input("Your guess was too high. Guess again. "))
        count += 1
    elif user_guess < comp_number:
        user_guess = int(input("Your guess was too low. Guess again. "))
        count += 1

while count == 3 and comp_number != user_guess:
    print("You LOSE! ")
    break

while comp_number == user_guess:
    print("You guessed correctly!")
    break
