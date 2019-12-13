import random

comp_number = random.randint(1,20)
count = 1

user_guess = int(input("Guess a number between 1-20. You have 3 tries. "))

while user_guess != comp_number and count < 3:
    if user_guess > comp_number:
        user_guess = int(input("Your guess was too high. Guess again. "))
        count += 1
    elif user_guess < comp_number:
        user_guess = int(input("Your guess was too low. Guess again. "))
        count += 1

if count == 3:
    print ("You LOSE! ")

    
print("You guessed correctly!")
