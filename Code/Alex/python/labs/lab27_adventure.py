'''
Lab 27: Adventure

Let's build a simple board game that runs on the terminal. We'll represent the board using a list of lists. We'll use two ints to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:

*- use more concise commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west)

*- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side

- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)

- loading a text file containing the map, or procedurally generate things

- walls / barriers

- use different unicode characters (you can find lists online)

- ascii art

- colorama for custom colors, or curses for even more control of the terminal

- add 'fog of war' - only show the elements of board immediately around the player (you can then find a torch item, which expands your visibility)

- have enemies move around

- add an inventory system

- add player health, more complex encounters

- add hidden treasure, make the objective to find all the treasure

- add a 'final boss' that you can only face once collecting items

- re-use previous labs (guess the number, rock-paper-scissors)
'''


import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_position_x = 4 #position in row the player is in
player_position_y = 4 #position in column the player is in

# add 4 enemies in random locations
for i in range(4):
    ''' I LEARNED SOMETHING. with range, the upperbound is exclusive. We put 4 because their are 4 enemies'''
    enemy_position_x = random.randint(0, height - 1) #puts enemy at a random spot in any row
    enemy_position_y = random.randint(0, width - 1) #puts enemy at a random spot in any column
    board[enemy_position_y][enemy_position_x] = '§' #creates and displays an enemy symbol for each enemy


# loop until the user says 'done' or dies
while True:

# print out the board
    for i in range(height): #for any space in row
        for j in range(width): #for any space in column
            if i == player_position_y and j == player_position_x: #if we're at the player location, print the player icon
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

# get the command from the user
    command = input('what is your command? ').lower()

    if command in ['done', 'quit', 'q', 'exit']:
        break  # exit the game
    elif command in ['left', 'l', 'west', 'w']:
        player_position_x -= 1  # move left
        if player_position_x not in range(len(board)):
            player_position_x = 9
            print(player_position_x, player_position_y)
    elif command in ['right', 'r', 'east', 'e']:
        player_position_x += 1  # move right
        if player_position_x not in range(len(board)):
            player_position_x = 0
    elif command in ['up', 'u', 'north', 'n']:
        player_position_y -= 1  # move up
        if player_position_y not in range(len(board)):
            player_position_y = 9
    elif command in ['down', 'd', 'south', 's']:
        player_position_y += 1  # move down
        if player_position_y not in range(len(board)):
            player_position_y = 0

# check if the player is on the same space as an enemy
    if board[player_position_y][player_position_x] == '§':
        print('you\'ve encountered an enemy!') #prompts the player
        action = input('what will you do? ') #gives them a choice
        if action == 'attack': #if they choose to attack
            print('you\'ve slain the enemy') #prompts user
            board[player_position_x][player_position_y] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')#prompts user
            break