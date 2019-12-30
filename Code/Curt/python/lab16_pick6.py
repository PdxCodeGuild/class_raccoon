#lab16_pick6.py
import random

def pick6():
    winval = []
    for x in range(6):
        value = random.randint(1,99)
        winval.append(value)
    return winval

def play_lottery():
    winning = pick6()
    balance = 0
    for x in range(100000):
        balance -= 2
        ticket = pick6()
    
