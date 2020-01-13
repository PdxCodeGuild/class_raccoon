import random
import sys

# Imported Snippet to Clear Screen:
# import call method from subprocess module
import os
from subprocess import call
from time import sleep
# define clear function
def clear():
	# check and make call for specific operating system
	_ = call('clear' if os.name =='posix' else 'cls')


width = 15  # the width of the board
height = 15  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list

#create top border
board.append([])
board[0].append('▒')
for j in range(width):
    board[0].append('▒')
board[0].append('▒')

#create board
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    board[i+1].append('▒')
    for j in range(width):  # loop over the columns
        board[i+1].append(' ')  # append an empty space to the board
    board[i+1].append('▒')

#create bottom border
board.append([])
board[-1].append('▒')
for j in range(width):
    board[-1].append('▒')
board[-1].append('▒')

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

#make some walls
walllength = 3
for i in range(5):
    wall_y,wall_x = random_gen(len(board[0]), len(board), board, '▒')
    for j in range(walllength):
        addwall = False
        if board[wall_y-1][wall_x] != ' ' and board[wall_y+1][wall_x] != ' ' and board[wall_y][wall_x-1] != ' ' and board[wall_y][wall_x+1] != ' ':
            addwall = True #breaks loop if no valid spaces for wall creation
        while not addwall:
            direction = random.randint(1,4) % 4
            if direction == 0:
                if board[wall_y-1][wall_x] == ' ':
                    wall_y -= 1
                    board[wall_y][wall_x] = '▒'
                    addwall = True
            elif direction == 1:
                if board[wall_y+1][wall_x] == ' ':
                    wall_y += 1
                    board[wall_y][wall_x] = '▒'
                    addwall = True
            elif direction == 2:
                if board[wall_y][wall_x-1] == ' ':
                    wall_x -= 1
                    board[wall_y][wall_x] = '▒'
                    addwall = True
            else:
                if board[wall_y][wall_x+1] == ' ':
                    wall_x += 1
                    board[wall_y][wall_x] = '▒'
                    addwall = True

# randomize the player starting position
player_y,player_x = random_gen(len(board[0]), len(board), board, '☺')

# add X enemies in random locations (currently set to 7)
enemycount = 0
for i in range(7):
    enemycount += 1
    enemy_y,enemy_x = random_gen(len(board[0]), len(board), board, '§')

# add swords in random locations:
for i in range(3):
    sword_y,sword_x = random_gen(len(board[0]), len(board), board, '⚔')
    sword = False #initialize sword

board[player_y][player_x] = ' ' #removes generated player marker
# loop until the user says 'done' or dies

#combat function
def combat(sword):
    #player's hp at full at start of combat
    playerhp = 100
    safetycount = 0
    safetydance = False
    wpnmultiplier = 1 #attack strength
    if sword:
        wpnmultiplier += 1
    #determine health & strength of enemy
    enemyhp = 70 + random.randint(10, 50)

    while playerhp > 0 and enemyhp > 0:
        #select a player action
        actionlist = ['a','attack','r','run','run away','safety dance']
        while True:
            action = input("What action would you like to take? \nATTACK / A\nRUN / R\n SAFETY DANCE\n").casefold()
            if action not in actionlist:
                print("Your enemy stares at you, contemplating whether it is worth its time to trifle with a moron.")
            else:
                break

        #player takes an action
        if action in ['attack','a']:
            print("You attack!")
            playeratk = wpnmultiplier * random.randint(1,10)
            enemyhp -= playeratk
            print(f"You do {playeratk} points of damage.")
            if enemyhp > 0:
                print(f"The enemy has {enemyhp} HP remaining.")
        if action in ['run','run away','r']:
            print ("You can't run, you coward!")
            sleep(1)
        if action == 'safety dance':
            chance = random.randint(1,5)
            if chance % 5 == 0:
                print("You acted like an imbecile.")
                sleep(.8)
                print("SAFETY DANCE FAILED!")
                input("Press ENTER to continue")
            else:
                print("You can dance if you want to.")
                sleep(.8)
                print("Your enemy doesn't dance.")
                sleep(.8)
                print("And if it doesn't dance, well,")
                sleep(.8)
                print("It's no friend of mine!")
                sleep(.8)
                print("SAFETY DANCE SUCCEEDED!")
                print("DEFENSE INCREASED")
                safetydance = True
                safetycount = 3
                sleep(1)
        # input()

        #enemy attacks
        if enemyhp > 0:
            print("The enemy attacks!")
            if safetycount > 0:
                defenseup = 1
                safetycount -= 1
            else:
                defenseup = 0
            enemyatk = random.randint(3,12)
            enemyatk = int(round(enemyatk - (enemyatk * .3 * defenseup), 0))
            playerhp -= enemyatk
            print(f"You take {enemyatk} points of damage.")
            if playerhp > 0:
                print(f"You have {playerhp} HP remaining.")
            if safetydance and safetycount <= 0:
                print("Your safety dance has worn off!")
                safetydance = False
            # input()

    if playerhp <= 0:
        win = False

    if enemyhp <= 0:
        win = True

    return win

while True:
    #DISPLAY THE BOARD
    clear() # Clears the screen before displaying the board
    for i in range(len(board)):
        for j in range(len(board[i])):
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
        if board[player_y][player_x] == '▒':
            print("Can't go there!")
            player_x += 1
            sleep(.8)
    elif command in ['right','r','east','e']:
        player_x += 1  # move right
        if board[player_y][player_x] == '▒':
            print("Can't go there!")
            player_x -= 1
            sleep(.8)
    elif command in ['up','u','north','n']:
        player_y -= 1  # move up
        if board[player_y][player_x] == '▒':
            print("Can't go there!")
            player_y += 1
            sleep(.8)
    elif command in ['down','d','south','s']:
        player_y += 1  # move down
        if board[player_y][player_x] == '▒':
            print("Can't go there!")
            player_y -= 1
            sleep(.8)

    #get the sword
    if board[player_y][player_x] == '⚔':
        clear()
        print("You got the sword!")
        board[player_y][player_x] = ' '
        sword = True
        sleep(1.5)

    # check if the player is on the same space as an enemy
    if board[player_y][player_x] == '§':
        print("You've encountered an enemy!")
        # action = input("What will you do? ")
        win = combat(sword)
        if win:
            print("You've slain the enemy!")
            board[player_y][player_x] = ' '  # remove the enemy from the board
            enemycount -= 1
            sleep(1.5)
        else:
            print("You have been slain!")
            sys.exit()

    # win conditions
    if enemycount == 0:
        print("Conglaturation !!!")
        print("You have completed a great game.")
        print("And prooved the Justice of our Culture.")
        print("Now go and rest our Heroes !")
        sys.exit()