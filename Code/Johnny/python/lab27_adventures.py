import random


class Look:
    # print out the board
    def __init__(self):
        for i in range(height):
            for j in range(width):
                # if we're at the player location, print the player icon
                if i == player_i and j == player_j:
                    print('🐇', end=' ')
                else:
                    print(board[i][j], end=' ')  # otherwise print the board square
            print()
    def look(self):
        for i in range(height):
            for j in range(width):
                # if we're at the player location, print the player icon
                if i == player_i and j == player_j:
                    print('🐇', end=' ')
                else:
                    print(board[i][j], end=' ')  # otherwise print the board square
            print()

class Battle_Roll:
# Begins functions inside class
    def __init__(self):
        self.currenthp = 10
        self.currentmana = 10

        self.hp = 10
        self.mana = 10


    def check_hp(self):
        print(f"STATUS: hp {self.currenthp}/{self.hp}, mana {self.currentmana}/{self.mana}")

    def hp_boost(self):
        self.hp += x

    def roll_dice(self):
        roll = random.randint(1, 10)
        print(roll)# -*- coding: utf-8 -*-

    def you_win(self):
        print(r"    _.----.        ____         ,'  _\   ___    ___     ____")
        print(r"\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
        print(r"\.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
        print(r"   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
        print(r"    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
        print(r"     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
        print(r"      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
        print(r"       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
        print(r"        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
        print(r"                                `'                            '-._|")

width = 5  # the width of the board
height = 5  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '🦁'

for i in range(1):
    stuff_i = random.randint(0, height - 1)
    stuff_j = random.randint(0, width - 1)
    board[stuff_i][stuff_j] = '^'

# loop until the user says 'done' or dies
battle = Battle_Roll()
look_board = Look()
moves_bar = ['left', 'right', 'down', 'up']
moves_bar2 = ['look', 'inv', 'status', 'or done']
inv_bar = []
enemy = 0

while True:
# need to add instructions to push out
    print('>>> '+', '.join(moves_bar)+' <<<')
    print('>>> '+', '.join(moves_bar2)+' <<<')
    command = input('what is your command? ').lower()  # get the command from the user

    if command == 'done':
        break # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player_j -= 1 # move left
    elif command in ['r', 'right', 'e', 'east']:
        player_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player_i += 1  # move down
    elif command == 'status':
        print(f'{battle.check_hp()}')
    elif command == 'look':
        look_board.look()
    elif command == 'inv':
        print(inv_bar)
    elif command == 'roll':
        print(battle.roll_dice())

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '🦁':
        print('> you\'ve encountered an enemy! <')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '
            enemy += 1 # remove the enemy from the board
            if enemy == height -1:
                battle.you_win()
                break
        else:
            print('you hestitated and were slain')
            print('GAME OVER')
            break
    elif board[player_i][player_j] == '^':
        x = 50
        battle.hp_boost()
        print(f'bonus + {x} hp')
        board[player_i][player_j] = ' '  # remove the ^ from the board
print(enemy)
