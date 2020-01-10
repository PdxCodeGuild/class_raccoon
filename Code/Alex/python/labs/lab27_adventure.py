'''
Lab 27: Adventure

Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists. We'll use two ints to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:

*- use more concise commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)

*- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side

*- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)

- have enemies move around

- walls / barriers

- add an inventory system

- add hidden treasure, make the objective to find all the treasure

- add player health, more complex encounters

- add a 'final boss' that you can only face once collecting items

- ascii art

- colorama for custom colors, or curses for even more control of the terminal

- loading a text file containing the map, or procedurally generate things

- use different unicode characters (you can find lists online)

- add 'fog of war' - only show the elements of board immediately around the player (you can then find a torch item, which expands your visibility)

- re-use previous labs (guess the number, rock-paper-scissors)
'''


import random

width = 6  # the width of the board
height = 20  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = random.randint(1, height - 2) #position in column the player is in
player_j = random.randint(1, width - 2) #position in row the player is in


# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(1, height - 2)
    enemy_j = random.randint(1, width - 2)
    board[enemy_i][enemy_j] = '§'

# loop until the user says 'done' or dies
while True:

#print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            elif i == 0 or i == height - 1:
                print('x', end=' ')
            elif j == 0 or j == width - 1:
                print('x', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

# get the command from the user
    command = input('what is your command? ').lower()

    if command in ['done', 'quit', 'q', 'exit']:
        break  # exit the game
    elif command in ['left', 'l', 'west', 'w']:
        player_j -= 1  # move left
        if player_j == 0:
            player_j = width - 2
        elif player_j == width - 1:
            player_j = 1
    elif command in ['right', 'r', 'east', 'e']:
        player_j += 1  # move right
        if player_j == 0:
            player_j = width - 2
        elif player_j == width - 1:
            player_j = 1
    elif command in ['up', 'u', 'north', 'n']:
        player_i -= 1  # move up
        if player_i == 0:
            player_i = height - 2
        elif player_i == height - 1:
            player_i = 1
    elif command in ['down', 'd', 'south', 's']:
        player_i += 1  # move down
        if player_i == 0:
            player_i = height - 2
        elif player_i == height - 1:
            player_i = 1
    else:
        print("not a valid command")
        input()

#check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break
