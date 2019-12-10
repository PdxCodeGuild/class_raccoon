#Random emoticon generator

import random

eyes = [":", ";", "8",]
nose = ["-",">","O"]
mouth = [")", "(", "P", "}"]



turn = 0

def generator():
    turn = 0
    while turn <= 5:
        eye = random.choice(eyes)
        noses = random.choice(nose)
        mouths = random.choice(mouth)
        turn += 1
        print(eye, noses, mouths)



print("Welcome to the emoticon generator. ")
generator()
