import random
import os
import sys
import time

width = 40  # the width of the board
height = 40  # the height of the board
entity_list = []
enemy_dict = {"҉":[10,0,1,1], "§":[80,12,18,4], "ß":[20,6,10,2], "ʘ":[40,30,40,10], "ˢ":[2, 2, 18, 2], "ѱ":[120,2,5,2]}
player = [100, 4, 8, 2]
heal = "╬"

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

class Map:
    def __init__(self,w,h):
        self.positions = []
        self.y = w -1
        self.x = h -1
        for i in range(h):
            self.positions.append([])
            for j in range(w):
                self.positions[i].append("-")

    def __str__(self):
        return "pls don't try to do this"

    def pos_check(self, position):
        return self.positions[position[0]][position[1]]

    def update(self, type, prev, current):
        if prev != None:
            self.positions[prev[0]][prev[1]] = "-"
        self.positions[current[0]][current[1]] = type

    def print_map(self, y, x, view=6):
        for i in range((y - view + self.y), (y + view + self.y)+1):
            for j in range((x - view + self.x), (x + view + self.x)+1):
                print(self.positions[(i+1)%(self.y+1)][(j+1)%(self.x+1)], end=" ")
                # print(f"[{i},{j}]", end=", " )
            print()


def collision(curr_ent, collided, collided_pos):
    if curr_ent.type == collided:
        return
    elif collided in enemy_dict or collided == "☺":
        if curr_ent.type == "☺":
            player_combat(curr_ent, collided_pos)
        else:
            enemy_combat(curr_ent, collided_pos)
    if collided == "ރ" and current.type == "☺":
        player_weapon = 1
        curr_ent.map.update(curr_ent.type, [curr_ent.y, curr_ent.x], collided)

class Entity:
    def __init__(self, map, y = 0, x = 0, type="ß", hp=20, lo=6, hi=10, mov=2):
        self.type = type
        self.hp = hp
        self.lo = lo
        self.hi = hi
        self.mov = mov
        self.y = y
        self.x = x
        self.map = map
        map.update(type,None,[y,x])

    def move(self, x, y):
        newpos = [(self.y + y + self.map.y+1)%(self.map.y+1), (self.x + x + self.map.x+1)%(self.map.x+1)]
        position_data = self.map.pos_check(newpos)
        if position_data == "-":
            self.map.update(self.type, [self.y, self.x], newpos)
            self.y = newpos[0]
            self.x = newpos[1]

        else:
            collision(self, position_data, newpos)

    def __str__(self):
        output = f"type: {self.type}, hp: {self.hp}, attack low: {self.lo}, attack high: {self.hi}, movement: {self.mov}, [y,x]: [{self.y},{self.x}]"
        return output

def player_combat(player, enemy_pos):
    for ent in entity_list:
        if enemy.x == enemy_pos[1] and enemy.y == enemy_pos[0]:
            enemy = ent
            break
    uschoice = input("you encounter an enemy, what do you do (attack, defend)?").lower()
    if uschoice in ["attack", "a"]:
        atkroll == random.randint(player.lo, player.hi)
        if player_weapon == 1:
            atkroll += random.randint(6,10)
        enemy.hp -= atkroll
        if enemy.hp < 1:
            entity_list.remove(enemy)
            player.map.update(player.type, enemy_pos, [player.y, player.x])
            input("you killed the enemy!")
        else:
            input("")
        print()
def enemy_combat(attacker, def_pos):
    pass

def ent_init(type, this_map):
    y = random.randint(0, this_map.y)
    x = random.randint(0, this_map.x)
    if type == "☺":
        entity_list.append(Entity(this_map, y, x, type, player[0], player[1], player[2], player[3]))
        return
    while y == entity_list[0].y and x == entity_list[0].x:
        y = random.randint(0, this_map.y)
        x = random.randint(0, this_map.x)
    if type == "ރ":
        entity_list.append(Entity(this_map, y, x, type))
        return
    entity_list.append(Entity(this_map, y, x, type, enemy_dict[type][0], enemy_dict[type][1], enemy_dict[type][2], enemy_dict[type][3]))

def mapgen(tumbleweed, dragon, skeleman, eye, snek, cactus, sword, wide, high):
    this_map = Map(wide, high)
    ent_init("☺", this_map)
    for i in range(tumbleweed):
        ent_init("҉", this_map)
    for i in range(dragon):
        ent_init("§", this_map)
    for i in range(skeleman):
        ent_init("ß", this_map)
    for i in range(eye):
        ent_init("ʘ", this_map)
    for i in range(snek):
        ent_init("ˢ", this_map)
    for i in range(cactus):
        ent_init("ѱ", this_map)
    for i in range(sword):
        ent_init("ރ", this_map)

mapgen(6, 1, 4, 1, 3, 12, 4, width, height)
turn = 0
player_weapon = 0
while True:
    if turn%entity_list[0].mov == 0:
        time.sleep(0.3)
    clear()
    entity_list[0].map.print_map(entity_list[0].y, entity_list[0].x, 6)
    print(entity_list[0])
    for ent in entity_list:
        if turn%ent.mov == 0:
            if ent.type == "☺":
                usin = input("what direction do you want to move (u,d,l,r)").lower()
                if usin in ["u","n","up","north"]:
                    ent.move(0,-1)
                elif usin in ["d","s","down","south"]:
                    ent.move(0, 1)
                elif usin in ["l","e","left","east"]:
                    ent.move(-1,0)
                elif usin in ["r","w","right","west"]:
                    ent.move(1,0)
            elif ent.type == "ѱ":
                pass
            elif ent.type == "҉":
                if turn%7 == 0:
                    ent.move(1,1)
                else:
                    ent.move(1,0)
            else:
                rand_d = random.randint(0,4)
                if rand_d == 1:
                    ent.move(0,-1)
                elif rand_d == 2:
                    ent.move(0, 1)
                elif rand_d == 3:
                    ent.move(-1,0)
                elif rand_d == 4:
                    ent.move(1,0)
    turn += 1
