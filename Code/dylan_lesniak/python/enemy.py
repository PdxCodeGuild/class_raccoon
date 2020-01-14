'''
Filename: lab27_enemy_class.py
Author: Dylan
Purpose: Origin code is getting cluttered. Creating enemy class to improve readability and useability. 
Will add features such as movement, health, and damage.
'''

import random

class Enemy:
    def __init__(self,height,width): 
        self.x_pos = 0
        self.y_pos = 0
        self.prev_y = self.y_pos
        self.prev_x = self.x_pos
        self.pos = [self.y_pos,self.x_pos]
        self.health = 10 
        self.height = height
        self.width = width

    def get_pos(self):
        self.y_pos = random.randint(0, self.height - 1)
        self.x_pos = random.randint(0, self.width - 1)
        self.pos = [self.y_pos,self.x_pos]
        while self.pos == [4,4]:
            self.y_pos = random.randint(0, self.height - 1)
            self.x_pos = random.randint(0, self.width - 1)
            self.pos = [self.y_pos,self.x_pos]

    def move(self):
        #this is gonna be a function where after every player turn, the enemy makes a turn. 
        #I'll make it random. I can probably just copy/paste the player turn function here, and just make it random. 
        self.prev_y = self.y_pos
        self.prev_x = self.x_pos
        inputs = ['w','a','s','d']
        command = random.choice(inputs)  # get the command from the user
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
        return 'y'

    def go_back(self):
        self.y_pos = self.prev_y
        self.x_pos = self.prev_x
        self.pos = [self.y_pos,self.x_pos]

    def damage(self, amount):
        self.health -= amount
        

    def __str__(self):
        return '| § |'

        #i should make the __str__ command return the character for the bad guy.
        #have its position accessible via some instance variables. 
        #then I can create a def move function/method I still don't remember the difference 