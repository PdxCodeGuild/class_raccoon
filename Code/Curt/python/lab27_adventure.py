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

#random generator for player, enemies, items, etc
def random_gen(width, height, board, symbol):
    conflict = True
    while conflict:
        unit_y = random.randint(0, height -1)
        unit_x = random.randint(0, width - 1)
        if board[unit_y][unit_x] != ' ':
            conflict = True
        else:
            board[unit_y][unit_x] = symbol
            conflict = False
    return unit_y, unit_x
# randomize the player starting position
player_y,player_x = random_gen(width, height, board, '☺')

# add 4 enemies in random locations
for i in range(4):
    enemy_y,enemy_x = random_gen(width, height, board, '§')

# add a sword in a random location:
sword_y,sword_x = random_gen(width, height, board, '⚔')

board[player_y][player_x] = ' ' #removes generated player marker
# loop until the user says 'done' or dies
while True:
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_y and j == player_x:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

    command = input("What is your command? ")  # get the command from the user
    if command in ['done','quit','exit']:
        break  # exit the game
    elif command in ['left','l','west','w']:
        player_x -= 1  # move left
        if player_x not in range(len(board[0])):
            print("Can't go there!")
            player_x += 1
    elif command in ['right','r','east','e']:
        player_x += 1  # move right
        if player_x not in range(len(board[0])):
            print("Can't go there!")
            player_x -= 1
    elif command in ['up','u','north','n']:
        player_y -= 1  # move up
        if player_y not in range(len(board)):
            print("Can't go there!")
            player_y += 1
    elif command in ['down','d','south','s']:
        player_y += 1  # move down
        if player_y not in range(len(board)):
            print("Can't go there!")
            player_y -= 1

    #get the sword
    if board[player_y][player_x] == '⚔':
        print("You got the sword!")
        board[player_y][player_x] = ' '
        sword = True

    # check if the player is on the same space as an enemy
    if board[player_y][player_x] == '§':
        print("You've encountered an enemy!")
        action = input("What will you do? ")
        if action == 'attack':
            print("You've slain the enemy!")
            board[player_y][player_x] = ' '  # remove the enemy from the board
        else:
            print("You hestitated and were slain!")
            break

            # print out the board
