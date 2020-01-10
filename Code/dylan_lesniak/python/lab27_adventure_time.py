
# Lab 27: Adventure
'''
Let's build a simple board game that runs on the terminal. We'll represent the board using a **list of lists**. We'll use two `int`s to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:
- use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west) * CHECK
- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side * CHECK
- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)
- loading a text file containing the map, or procedurally generate things
- walls / barriers * CHECK
- use different unicode characters (you can find [lists online](https://www.google.com/search?q=cool+unicode+characters&rlz=1C1CHBF_enUS773US773&oq=cool+unicode+chara&aqs=chrome.0.0j69i57j0l3.90708j1j1&sourceid=chrome&ie=UTF-8))
- ascii art
- [colorama](https://pypi.python.org/pypi/colorama) for custom colors, or [curses](https://docs.python.org/3/howto/curses.html) for even more control of the terminal
- add 'fog of war' - only show the elements of board immediately around the player (you can then find a torch item, which expands your visibility)
- have enemies move around 
- add an inventory system
- add player health, more complex encounters
- add hidden treasure, make the objective to find all the treasure
- add a 'final boss' that you can only face once collecting items
- re-use previous labs (guess the number, rock-paper-scissors)


''' 

import random
import helper
import pdb
import sys

class Game:
    def __init__(self):
        self.width = 10  # the width of the board
        self.height = 10  # the height of the board

        # create a board with the given width and height
        # we'll use a list of list to represent the board
        self.board = []  # start with an empty list
        # define the player position
        self.player_pos = {"y": 4, "x": 4} #i is y-axis. j is x-axis.
        self.enemy_pos = {}

    def create_board(self):
        for i in range(self.height):  # loop over the rows
            self.board.append([])  # append an empty row
            for j in range(self.width):  # loop over the columns
                self.board[i].append(f'|   |')  # append an empty space to the board


        # add 4 enemies in random locations
    def add_enemies(self):
        for i in range(4): #self.enemy_pos is a dictionary with a list as a value. I hope. 
            self.enemy_pos[i] = []
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)
            self.enemy_pos[i].append(y)
            self.enemy_pos[i].append(x)
            while self.board[y][x] == '| § |': #or self.enemy_pos[i] == [4,4]: #just can't be player pos at creation
                self.enemy_pos[i] = []
                y = random.randint(0, self.height - 1)
                x = random.randint(0, self.width - 1)
                self.enemy_pos[i].append(y)
                self.enemy_pos[i].append(x)
            self.board[y][x] = '| § |' #board[position] = "bad-guy character"

        #move print statement here. 
            # print out the board
    def print_board(self):
        for i in range(self.height): #for the y axis
            for x in range(self.width):
                print("-----", end=" ")
            print()
            for j in range(self.width): #for the x axis
                # if we're at the player location, print the player icon
                if i == self.player_pos['y'] and j == self.player_pos['x']: #if the current printable position is the player position
                    print('| ☺ |', end=' ') #print player 
                else:
                    print(self.board[i][j], end=' ')  # otherwise print the board square
            print()
            for i in range(self.width):
                print("-----", end=" ")
            print()
        
        # loop until the user says 'done' or dies
    def take_turn(self):
        while True:
            self.print_board()
            inputs = ['w','a','s','d']
            command = helper.text_checker(input('what is your command? (w/a/s/d): '),inputs)  # get the command from the user

            if command == 'done':
                break  # exit the game
            elif command in ['a']:
                if self.player_pos['x'] > 0:
                    self.player_pos['x'] -= 1  # move left
            elif command in ['d']:
                if self.player_pos['x'] < self.width - 1:
                    self.player_pos['x'] += 1  # move right
            elif command in ['w']:
                if self.player_pos['y'] > 0:
                    self.player_pos['y'] -= 1  # move up
            elif command in ['s']:
                if self.player_pos['y'] < self.width - 1:
                    self.player_pos['y'] += 1  # move down

            # check if the player is on the same space as an enemy
            if self.board[self.player_pos["y"]][self.player_pos["x"]] == '| § |': #if the inteded location of the player already has a bad guy, enter encounter
                print('you\'ve encountered an enemy!')
                action = helper.text_checker(input('what will you do? (attack/run) '),["attack","run"])
                if action == 'attack': 
                    print('you\'ve slain the enemy')
                    self.del_enemy(self.player_pos["y"], self.player_pos["x"])
                    self.board[self.player_pos["y"]][self.player_pos["x"]] = '|   |'  # remove the enemy from the board
                else:
                    print('you hestitated and were slain') 
                    break

    def del_enemy(self, y, x):
        i = 0 
        for enemy in self.enemy_pos:
            if self.enemy_pos[enemy] == [y,x]:
                self.enemy_pos.pop(enemy)
                break
        self.end_game_check()

    def end_game_check(self):
        if len (self.enemy_pos) <= 0:
            print('YOU WON THE GAME. YOU THE HERO. Y33T')
            input()
            sys.exit()

    def run(self):
        self.create_board()
        self.add_enemies()
        self.take_turn()

if __name__ == "__main__":
    new_game = Game()
    new_game.run()