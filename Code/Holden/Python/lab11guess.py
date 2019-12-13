import random

while True:
    usin = "-1"
    limit=input("how large of a number do you want to guess(exit to quit): ").lower()
    if limit == "exit" or limit == "quit":
        break
    if not limit.isdigit():
        print("Please enter a positive number.")
        continue
    comp = random.randint(1,int(limit))
    exit = False
    looped = False
    count = 0
    while True:
        count += 1
        usin = input("Guess a number between 1 and "+limit+": ").lower()
        if usin == "exit" or usin == "quit":
            exit = True
            break
        if not usin.isdigit():
            print("Please enter a positive number.")
            usin = "-1"
            continue
        if int(usin) == comp:
            print(f"Correct! you guessed it in {count} tries.")
            break
        elif int(usin) > comp:
            print("Too high", end="")
        elif int(usin) < comp:
            print("Too low", end="")
        usindist = abs(int(usin) - comp)
        if looped == True:
            if lastin == usindist:
                print(", and the same distance away.")
            elif lastin > usindist:
                print(", and closer.")
            elif lastin < usindist:
                print(", and further.")
        else:
            print(".")
            looped = True
        lastin = usindist
    if exit == True:
        break
