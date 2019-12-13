import random
#counter
counter = 0
while counter < 10:
    player_var = int(input("Guess a number between 1 - 10? "))
    print(f"Player guesses {player_var}.")
    computer_var = random.randint(1, 10)
    print(f"Computer's number is {computer_var}.")
    i = player_var
    j = computer_var
    counter = counter + 1
    if i == j:
        print(f"You won! {counter} tries. ")
else:
    print(f"That's {counter} tries. \n"
        "Thanks for playing")
