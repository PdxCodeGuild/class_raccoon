'''
Filename: player.py
Author: Dylan 
Purpose: create a player class. Will have functions such as move and variables such as position and health. 
Class gives us flexibility to add more functionality later. 
'''

import helper
import sys

class Player():
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.y_pos = (self.height - 1) // 2
        self.x_pos = (self.height - 1) // 2 
        self.prev_y = self.y_pos
        self.prev_x = self.x_pos
        self.pos = [self.y_pos,self.x_pos]
        self.health = 100 

    def take_turn(self): 
        inputs = ['w','a','s','d']
        command = helper.text_checker(input('what is your command? (w/a/s/d): '),inputs)  # get the command from the user
        if command == 'done':
            return 'n'  # exit the game
        elif command in ['a']:
            if self.x_pos > 0:
                self.x_pos -= 1  # move left
                self.pos = [self.y_pos,self.x_pos]
        elif command in ['d']:
            if self.x_pos < self.width - 1:
                self.x_pos += 1  # move right
                self.pos = [self.y_pos,self.x_pos]
        elif command in ['w']:
            if self.y_pos > 0:
                self.y_pos -= 1  # move up
                self.pos = [self.y_pos,self.x_pos]
        elif command in ['s']:
            if self.y_pos < self.width - 1:
                self.y_pos += 1  # move down
                self.pos = [self.y_pos,self.x_pos]
        return 'y' #take_turn in lab27 is made to have a checker if the game is still continuing. 
    
    def damage(self, amount):
        self.health -= amount

    def print_health(self):
        print(f"Health: {self.health}")