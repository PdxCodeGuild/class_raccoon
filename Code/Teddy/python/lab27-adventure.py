'''
Lab 27: Adventure
Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists.
We'll use two ints to represent that player's position on the board. Every iteration of the game loop,
the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:

- use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)
- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side
- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)
- loading a text file containing the map, or procedurally generate things
- walls / barriers
- use different unicode characters (you can find lists online)
- ascii art
- colorama for custom colors, or curses for even more control of the terminal
- add 'fog of war' - only show the elements of board immediately around the player
(you can then find a torch item, which expands your visibility)
- have enemies move around
- add an inventory system
- add player health, more complex encounters
- add hidden treasure, make the objective to find all the treasure
- add a 'final boss' that you can only face once collecting items
- re-use previous labs (guess the number, rock-paper-scissors)
'''

import random
fire = '🔥'
dragon = '🐲'
burger = '🍔'
mushroom = '🍄'
apple = '🍏'
fries = '🍟'
player1 = '👶'
player2 = '👦'
player3 = '🤴'

width = 30  # the width of the board
height = 30  # the height of the board
# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        random_fire = random.randint(1, width - 2)

        random_dragon = random.randint(1, width - 2)

        if j == random_fire:
            board[i].append(fire)
        elif j == random_dragon:
            board[i].append(dragon)

        else:
            board[i].append('. ')  # append an empty space to the board

# define the player position
player_i = 15
player_j = 15

# add enemies in random locations
for i in range(4):
    enemy_i = random.randint(1, height - 2)
    enemy_j = random.randint(1, width - 2)
    board[enemy_i][enemy_j] = burger

for i in range(4):
    enemy_i = random.randint(1, height - 2)
    enemy_j = random.randint(1, width - 2)
    board[enemy_i][enemy_j] = mushroom
for i in range(4):
    enemy_i = random.randint(1, height - 2)
    enemy_j = random.randint(1, width - 2)
    board[enemy_i][enemy_j] = apple

for i in range(4):
    enemy_i = random.randint(1, height - 2)
    enemy_j = random.randint(1, width - 2)
    board[enemy_i][enemy_j] = fries

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? (u/d/l/r for up/down/left/right or done) ').lower()  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l','left']:
        player_j -= 1  # move left
        if player_j == 0: # if player at the end of left
            player_j = width - 1 # move a player to the right of the board

    elif command in ['r','right']:
        player_j += 1  # move right
        if player_j == width:  # if player at the end of right
            player_j = 0 # move a player to the left of the board
    elif command in ['u','up']:
        player_i -= 1  # move up
        if player_i == 0: # if player at the top of board
            player_i = height - 1 # move a player to bottom of the board
    elif command in ['d','down']:
        player_i += 1  # move down
        if player_i == height: # if player at the bottom of board
            player_i = 0 # move a player to top of the board

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == burger or board[player_i][player_j] == mushroom or board[player_i][player_j] == apple or board[player_i][player_j] == fries:
        print('you\'ve found a food!')
        action = input('Do you want to eat (y/n)?  ').lower()
        if action == 'yes' or  action == 'y':
            print('Get bigger soon, Go eat more')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('You skinny as hell')

    if board[player_i][player_j] == fire:
        print(f'You got burn by {fire}')
        print()
        break
    elif board[player_i][player_j] == dragon:
        print(f'You got burn by {dragon}')
        print()
        break

    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(player1, end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()
