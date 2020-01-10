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

width = 60  # the width of the board
height = 60  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for x in range(width):  # loop over the rows
    board.append([])  # append an empty row
    for y in range(height):  # loop over the columns
        board[x].append(' ')  # append an empty space to the board

# define the player position
player_position_x = random.randint(1, width - 2) #position in row the player is in
player_position_y = random.randint(1, height - 2) #position in column the player is in

# add 4 enemies in random locations
for coordinate in range(100):
    ''' I LEARNED SOMETHING. with range, the upperbound is exclusive. We put 4 because their are 4 enemies'''
    enemy_position_x = random.randint(1, width - 2) #puts enemy at a random spot in any row
    enemy_position_y = random.randint(1, height - 2) #puts enemy at a random spot in any column
    board[enemy_position_x][enemy_position_y] = '§' #creates and displays an enemy symbol for each enemy


# loop until the user says 'done' or dies
while True:

# print out the player position and 10 spaces in all directions of that position
    for x in range(max(0, player_position_x - 10), min(width, player_position_x + 10)):
        for y in range(max(0, player_position_y - 10), min(height, player_position_y + 10)):
            if x == player_position_x and y == player_position_y: #if we're at the player location, print the player icon
                print('☺', end=' ')
            elif x == 0 or x == width - 1:
                print('x', end=' ')
            elif y == 0 or y == height - 1:
                print('x', end=' ')
            else:
                print(board[x][y], end=' ')  # otherwise print the board square
        print()

# get the command from the user
    command = input('what is your command? ').lower()

    if command in ['done', 'quit', 'q', 'exit']:
        break  # exit the game
    elif command in ['left', 'l', 'west', 'w']:
        player_position_y -= 1  # move left
        if player_position_y not in range(1, len(board) - 2):
            player_position_y = width - 2
            # print(player_position_x, player_position_y)
    elif command in ['right', 'r', 'east', 'e']:
        player_position_y += 1  # move right
        if player_position_y not in range(1, len(board) - 2):
            player_position_y = 1
    elif command in ['up', 'u', 'north', 'n']:
        player_position_x -= 1  # move up
        if player_position_x not in range(1, len(board) - 2):
            player_position_x = height - 2
    elif command in ['down', 'd', 'south', 's']:
        player_position_x += 1  # move down
        if player_position_x not in range(1, len(board) - 1):
            player_position_x = 1
    else:
        print("not a valid command")
        input()

# check if the player is on the same space as an enemy
    if board[player_position_x][player_position_y] == '§':
        print('you\'ve encountered an enemy!') #prompts the player
        action = input('what will you do? ') #gives them a choice
        if action == 'attack': #if they choose to attack
            print('\nyou\'ve slain the enemy') #prompts user
            board[player_position_x][player_position_y] = ' '  # remove the enemy from the board
        else:
            print('\nyou hestitated and were slain')#prompts user
            break
        input()