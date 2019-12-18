#montyhall.py
import random

prize = ["car","sheep","sheep"]

shuffledoor = prize
random.shuffle(shuffledoor)

pickdoor = random.randint(1,3)
