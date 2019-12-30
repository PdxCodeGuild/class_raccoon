#montyhall.py
import random

prize = ["car","sheep","sheep"]
doornum = [num for num in range(1,4)]

wincount = [0,0]
for x in range(100000):
    shuffledoor = prize
    random.shuffle(shuffledoor)

    doordict = {doornum[i]: shuffledoor[i] for i in range(len(doornum))}

    pickdoor = random.randint(1,3)
    pickprize = doordict[pickdoor]

    revealdoor = []
    for x in doordict:
        if x != pickdoor:
            if doordict[x] == "sheep":
                revealdoor.append(x)
    revealdoor = random.choice(revealdoor)

    for x in doordict:
        if x != pickdoor and x != revealdoor:
            switchdoor = x

    didswitch = [pickdoor, switchdoor]
    didswitch = random.choice(didswitch)
    if didswitch == pickdoor:
        switched = False
        if doordict[didswitch] == "car":
            wincount[0] += 1
            print("Didn't switch, won a car.")
        else:
            print("Didn't switch, won a sheep.")
    else:
        switched = True
        if doordict[didswitch] == "car":
            wincount[1] += 1
            print("Switched, won a car.")
        else:
            print("Switched, won a sheep.")
    print(wincount)

wincountratio = int(((wincount[1]/(wincount[0]+wincount[1]))*100))
print(f"After 10,000 random attempts, I won {wincount[0]} times when I didn't switch doors. I won {wincount[1]} times when I did. Thus I won {wincountratio} percent of the time when I switched doors.\n\nIn conclusion, always switch doors.")
