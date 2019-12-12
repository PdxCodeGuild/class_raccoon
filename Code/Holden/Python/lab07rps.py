import random
second_loop=""
input("Let's play rock, paper, scissors, lizard, spock.")
while True:
    player_choice=input("Please input your choice; rock, paper, scissors, lizard, or spock"+second_loop+": ").lower()
    if player_choice == "exit":
        break
    rpslist=["rock", "paper", "scissors", "spock", "lizard"]
    if player_choice not in rpslist:
        input("Please chooose a valid input.")
        continue
    computer = random.choice(rpslist)
    if player_choice == computer:
        outcome = " We tied."
    else:
        choice_index=rpslist.index(player_choice)
        rpslist.remove(player_choice)
        if choice_index%2 == rpslist.index(computer)%2:
            outcome = " You lose."
        else:
            outcome = " You win."
    print("I chose "+computer+"."+outcome)
    second_loop = " (or input exit to exit)"
