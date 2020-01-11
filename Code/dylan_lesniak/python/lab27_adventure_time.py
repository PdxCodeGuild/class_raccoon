
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
import enemy
import player

class Game:
    def __init__(self):
        self.width = 10  # the width of the board
        self.height = 10  # the height of the board

        # create a board with the given width and height
        # we'll use a list of list to represent the board
        self.board = []  # start with an empty list
        # define the player position
        self.me = None #will be initialized after the board is
        self.enemies = []
        self.enemy_positions = []

    def create_board(self):
        for i in range(self.height):  # loop over the rows
            self.board.append([])  # append an empty row
            for j in range(self.width):  # loop over the columns
                self.board[i].append(f'|   |')  # append an empty space to the board
    
    def create_player(self):
        self.me = player.Player(self.height,self.width)
        y = self.me.y_pos
        x = self.me.x_pos
        self.board[y][x] = '| ☺ |'
    
        # add 4 enemies in random locations
    def add_enemies(self):
        for i in range(4): #self.enemies is a dictionary with a list as a value. I hope. 
            self.enemies.append(enemy.Enemy(self.height,self.width)) #initializes an Enemy class. 
            self.enemies[i].get_pos()
            for bad_guy in self.enemies:
                if self.enemies[i].pos == bad_guy.pos: #is the current position the same as any other enemy's? if so, choose again
                    self.enemies[i].get_pos()
            y = self.enemies[i].y_pos
            x = self.enemies[i].x_pos
            self.board[y][x] = '| § |' #board[position] = "bad-guy character"
            self.enemy_positions.append([y,x])

        #move print statement here. 
            # print out the board
    def print_board(self):
        for i in range(self.height): #for the y axis
            for x in range(self.width):
                print("-----", end=" ")
            print()
            for j in range(self.width): #for the x axis
                print(self.board[i][j], end=' ')  #prints board square. Enemy and player pos should already be set. 
            print()
        for i in range(self.width):
            print("-----", end=" ")
        print()
        
        # loop until the user says 'done' or dies
    def take_turn(self):
        cont = 'y'
        while cont == 'y': #call my functions and have them change cont if a lose-condition is met. 
            self.me.print_health()
            self.print_board()
            cont = self.player_turn()
            # input("ENEMY TURN")
            self.bad_guy_turn()
            # self.print_board()

    #to make sure the player and bad guy stay in their positions in case of attack, store a prev_pos variable. 
    def bad_guy_turn(self):
        print("ENEMY TURN")
        for i in range(len(self.enemies)):
            self.reset_pos(self.enemies[i].y_pos, self.enemies[i].x_pos)
            self.enemies[i].move()
            while self.enemies[i].pos in self.enemy_positions: #this section makes them go back and choose another spot 
            #if spot occupied by another enemy
                self.enemies[i].go_back
                self.enemies[i].move()
            if self.enemies[i].pos == self.me.pos:
                self.combat("bad_guy")
                self.enemies[i].go_back()
                self.update_pos(self.enemies[i].y_pos, self.enemies[i].x_pos, '| § |')
            else:
                self.update_pos(self.enemies[i].y_pos, self.enemies[i].x_pos, '| § |')
                self.enemy_positions[i] = [self.enemies[i].y_pos,self.enemies[i].x_pos]
        
            

    def player_turn(self):
        cont = 'y'
        self.reset_pos(self.me.y_pos, self.me.x_pos) #clears current position so we don't wind up with duplicate player chars.
        cont = self.me.take_turn()
        if self.board[self.me.y_pos][self.me.x_pos] == '| § |': # check if the player is on the same space as an enemy
            cont = self.combat("player") #enters combat before enemy character's representation is deleted
            #I'm gonna need a way to reset the player position in case of multi-turn combat
        self.update_pos(self.me.y_pos,self.me.x_pos,'| ☺ |')
        return cont

    def reset_pos(self, y, x):
        self.board[y][x] = '|   |'
    
    def update_pos(self, y, x, char):
        self.board[y][x] = char
            
    def combat(self, attacker):
        if attacker == "player":
            print('you\'ve encountered an enemy!')
            print('Attack!!!')
            return self.damage_enemy()
        else:
            amount = 40
            print("An enemy attacked you.")
            print(f"You received {amount} damage.")
            input("Click ENTER")
            self.me.damage(amount)
            self.health_check()
        return 'y'

    def health_check(self):
        if self.me.health <= 0:
            print("YOU LOOOOOSE! LOLOLOLOLOLOL")
            sys.exit()

    def damage_enemy(self):
        i = 0 
        for bad_guy in self.enemies:
            if bad_guy.pos == [self.me.y_pos,self.me.x_pos]:
                amount = 40
                print(f"You dealt {amount} damage.")
                self.enemies[i].damage(10)
                if self.enemies[i].health <= 0:
                    print("ENEMY DEFEATED")
                    self.del_enemy()
                    input("Click ENTER")
                    break
            i += 1
        
        return self.end_game_check()

    def del_enemy(self):
        i = 0 
        for bad_guy in self.enemies:
            if bad_guy.pos == [self.me.y_pos,self.me.x_pos]:
                self.enemies.pop(i)
                break
            i += 1
        return self.end_game_check()

    def end_game_check(self):
        if len (self.enemies) <= 0:
            print('YOU WON THE GAME. YOU THE HERO. Y33T')
            sys.exit()
        else:
            return 'y'

    def run(self):
        self.create_board()
        self.create_player()
        self.add_enemies()
        # self.print_board()
        self.take_turn()

if __name__ == "__main__":
    new_game = Game()
    new_game.run()