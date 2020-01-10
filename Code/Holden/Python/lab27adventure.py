import random
import os
import sys

width = 30  # the width of the board
height = 30  # the height of the board
player_start = [random.randint(0,width-1),random.randint(0,height-1)]
entity_list = []
enemy_dict = {"҉":[10,0,1,1], "§":[80,12,18,4], "ß":[20,6,10,2], "ʘ":[40,30,40,10], "ˢ":[2, 2, 18, 2], "ѱ":[120,2,5,2]}
player = {"☺":[100, 4, 8, 2]}



class map:
    def __init__(self,w,h):
        self.positions = []
        self.x = w
        self.y = h
        for i in range(h):
            self.positions.append([])
            for j in range(w):
                self.positions[i].append("░")

    def pos_check(self, position):
        return self.positions[position[0]][position[1]]

    def update(self, type, prev=player_start, current):
        self.positions[prev[0]][prev[1]] = "░"
        self.positions[current[0]][current[1]] = type

def conflict(curr_ent, collided, collided_pos):
    if curr_ent.type == collided:
        return
    elif collided in enemy_dict or collided == "☺":
        if curr_ent.type == "☺":
            player_combat(curr_ent, collided_pos)
        else:
            enemy_combat(curr_ent, collided_pos)
    if collided == "ރ" and current.type == "☺":
        player_weapon = 1
        curr_ent.map.update(curr_ent.type, [curr_ent.x, curr_ent.y], collided)

class entity:
    def __init__(self, type="ß", hp=20, lo=6, hi=10, mov=1, map=standard_map, x, y):
        self.type = type
        self.hp = hp
        self.lo = lo
        self.hi = hi
        self.mov = mov
        self.x = x
        self.y = y
        self.map = map
        map.update(type,[x,y])

    def move(self, x, y):
        newpos = [(self.x + x)%self.map.x, (self.y + y)%self.map.y]
        position_data = self.map.pos_check(newpos)
        if position_data == "░":
            self.map.update(self.type, [self.x, self.y], newpos)
        else:
            conflict(self, position_data, newpos)

def player_combat(player, enemy_pos):
    pass
def enemy_combat(attacker, def_pos):
    pass
