
import re
import random

# player - name, chips
# [{'name': 'joe', 'chips': 3}, {'name': 'jill', 'chips': 3}]




#  1) get the player names from the user, build list of dictionaries
#  2) initialize the pot to 0
#  3) shuffle the players list
#  4) for each player
#  5) figure out the number of dice rolls given the player's number of chips
#  6) for each dice roll, pick L, C, R, or .
#  7) if the roll is ., do nothing
#  8) if the roll is L, move a player's chip to the player on the left
#  9) if the roll is C, move a player's chip to pot
# 10) if the roll is R, move a player's chip to the player on the right
# -----
# 11) check if any player won, if they did print the player's name and exit

player_names = 'matthew, teddy, tim,     , , , , ,curt' # input('Please enter all players: ')
player_names = re.split(r'[ ,]+', player_names)

die_faces = ['L', 'C', 'R', '.', '.', '.']

players = []
for player_name in player_names:
    player_dict = {'name':player_name, 'chips': 3}
    players.append(player_dict)

pot_chips = 0

random.shuffle(players)

current_player_index = 0
while True:
    player = players[current_player_index]
    rolls = min(player['chips'], 3)
    
    # rolls = 3
    # if player['chips'] < 3:
    #     rolls = player['chips']
    
    for x in range(rolls):
        roll = random.choice(die_faces)
        print(player['name'] + ' rolled a ' + roll)
        if roll == 'L':
            player['chips'] -= 1
            players[current_player_index-1]['chips'] += 1
        elif roll == 'R':
            player['chips'] -= 1
            players[(current_player_index+1)%len(players)]['chips'] += 1
        elif roll == 'C':
            player['chips'] -= 1
            pot_chips += 1
    
    for player in players:
        print(player['name'], player['chips'])
    print()
    
    if player['chips'] == 0:
        for i in range(len(players)):
            if players[i]['chips'] + pot_chips == len(players)*3:
                print(f'{players[i]["name"]} is the ultimate champion!')
                exit()
    
    
    current_player_index  = (current_player_index + 1) % len(players)
    


# while True:
#     for i in range(len(players)):
#         players[i]
#         players[i-1]
#         players[(i+1)%len(players)]



    
    
