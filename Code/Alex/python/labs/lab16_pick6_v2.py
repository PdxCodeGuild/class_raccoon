''' *not complete*
Lab 16: Pick 6

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
'''

import random


def pick6():
    npc = []
    for x in range(6):
        value = random.randint(1,99)
        npc.append(value)
    return npc

def num_matches(winning, ticket):
    count = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            count += 1
    return count

    # returns the number of matches between the two given lists

def play_lottery():
    payout = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
    }
    winning_counts = [0,0,0,0,0,0,0]
    winning = pick6()
    balance = 0
    for x in range(1000000):
        balance -= 2
        ticket = pick6()
        matches = num_matches(winning, ticket)
        winning_counts[matches] += 1
        balance += payout[matches]
        # print(f"${balance}")
        if x%100 == 0:
            print(winning_counts)
    return balance
print(play_lottery())

# print(pick6())
# print(num_matches([1,2,3], [2,2,4]))



# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
