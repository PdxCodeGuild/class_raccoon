'''
Filename: lab05_emoticon.py
Author: Dylan
Purpose: To randomly create an emoticon
'''

#mods
import random
#variables
eyes = [":",";","8","X","x","B"]
noses = ["^",""," ","-"]
mouths = [")","D","(","()","*","$"]
#functions
def create_con():
    emoticon = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    print(emoticon)

def five_cons():
    i = 0
    while i < 5:
        create_con()
        i += 1

five_cons()