import random
#counter
counter = 0
computer_var = random.randint(1, 10)
while counter < 10:
    counter = counter + 1
    player_var = int(input("Guess a number between 1 - 10? "))
    print(f"Player guesses {player_var}.")
    i = player_var
    j = computer_var
    k = player_var - computer_var
    if i < j:
        print("Too low.")
    elif i > j:
        print("Too high.")
    elif i == j:
        print(f"Computer's number is {computer_var}.")
        print(f"You won! {counter} tries. ")
        break
else:
    print(f"That's {counter} tries. \n"
        "Thanks for playing")
