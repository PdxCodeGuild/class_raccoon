# Lab 27: Adventure
'''
Let's build a simple board game that runs on the terminal. We'll represent the board using a **list of lists**. We'll use two `int`s to represent that player's position on the board. Every iteration of the game loop, the user will be prompted for a command. Start with the code below, and add your own modifications.

Possible modifications:
- use more succinct commands (l/u/d/r for up/down/left/right or n/s/e/w for north/south/east/west) -done
- add boundaries to the map, when the player attempts to move beyond the boundary, stop them or move them to the other side
- make what's printed on the screen a part of a much larger map (with the player always shown at the center of the screen)
- loading a text file containing the map, or procedurally generate things
- walls / barriers
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


```python
'''

import random
from os import system



class Player:
    def __init__(self):
        self.health = random.randint(30,50)
        self.melee = random.randint(20,30)
        self.spell = random.randint(30,50)
    def potion(self):
        return random.randint(30,50)

class Monster:
    def __init__(self):
        self.health = random.randint(30,50)
    def melee(self):
        return random.randint(10,20)
    def spell(self):
        return random.randint(20,30)
    def new_monster(self):
        self.health = random.randint(30,50)
        return self.health

# Initializing the player, monsters, and battle count
player1 = Player()
monster1 = Monster()
battle_count = 4

# text for the end of each turn
def turn_end():
    print(f'The monster has {monster1.health} hit points left')
    player1.health = player1.health - random.choice([monster1.melee(), monster1.spell()])
    print(f'You have {player1.health} hit points left')

# adds a pausing spot before clearing the board
def moving_along():
    input('hit <Enter> to continue')

# Creating a random new monster for each battle
def new_monster_init():
    if monster1.health <= 0:
        monster1.health = random.randint(30,50)
        return monster1.health
monster_pics = [r'''
               (    )
              ((((()))
              |o\ /o)|
              ( (  _')
               (._.  /\__
              ,\___,/ '  ')
'.,_,,       (  .- .   .    )
 \   \\     ( '        )(    )
  \   \\    \.  _.__ ____( .  |
   \  /\\   .(   .'  /\  '.  )
    \(  \\.-' ( /    \/    \)
     '  ()) _'.-|/\/\/\/\/\|
         '\\ .( |\/\/\/\/\/|
           '((  \    /\    /
           ((((  '.__\/__.')
            ((,) /   ((()   )
             "..-,  (()("   /
        pils  _//.   ((() ."
      _____ //,/" ___ ((( ', ___
                       ((  )
                        / /
                      _/,/'
                    /,/,"''',
r'''        .-"""".
   /       \
__ /   .-.  .\
/  `\  /   \/  \
|  _ \/   .==.==.
| (   \  /____\__\
\ \      (_()(_()
\ \            '---._
 \                   \_
/\ |`       (__)________/
/  \|     /\___/
|    \     \||VV
|     \     \|"""",
|      \     ______)
\       \  /`
     \()''',
r'''            _,--~~~,
                   .'        `.
                   |           ;
                   |           :
                  /_,-==/     .'
                /'`\*  ;      :
              :'    `-        :
              `~*,'     .     :
                 :__.,._  `;  :
                 `\'    )  '  `,
                     \-/  '     )
                     :'          \ _
                      `~---,-~    `,)
      ___                   \     /~`\
\---__ `;~~~-------------~~~(| _-'    `,
---, ' \`-._____     _______.---'         \
\--- `~~-`,      ~~~~~~                     `,
\----      )                                   \
\----.  __ /                                    `-
\----'` -~____
           ~~~~~--------,.___
                             ```\_''', r'''                                               ____
   ___                                      .-~. /_"-._
  `-._~-.                                  / /_ "~o\  :Y
      \  \                                / : \~x.  ` ')
       ]  Y                              /  |  Y< ~-.__j
      /   !                        _.--~T : l  l<  /.-~
     /   /                 ____.--~ .   ` l /~\ \<|Y
    /   /             .-~~"        /| .    ',-~\ \L|
   /   /             /     .^   \ Y~Y \.^>/l_   "--'
  /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
 Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
 |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
 |      ~---~           /   ~~"---\_  ' __[>
 l  .                _.^   ___     _>-y~
  \  \     .      .-~   .-~   ~>--"  /
   \  ~---"            /     ./  _.-'
    "-.,_____.,_  _.--~\     _.-~
                ~~     (   _}
                        `. ~(
                          )  \
                         /,`--'~\--''']


# removes monster from board when dead
def ded_monster():
    if monster1.health <= 0:
        global battle_count
        board[player_i][player_j] = ' '  # remove the enemy from the board
        print('You have vanquished the monster! Good jorb!')
        input('hit <Enter> to continue\n>')
        battle_count -= 1
        return monster1.health
        return battle_count

# breaks out of program when player dies
def ur_ded():
    print('Well, you\'re dead now. Byeeee')
    input('hit <Enter> to continue\n>')
    system('cls')

# Guts of the battle
def battle():
    print(random.choice(monster_pics))
    print(f'you\'ve encountered an enemy with {monster1.health} hit points!')

    while player1.health > 0:
        action = input('what will you do? (melee/m, spell/s, potion/p or run/r)\n> ')

        if action in ['melee', 'm']:
            print(random.choice([f'You swing your sword and do {player1.melee} damage', f'You slash and do {player1.melee} damage', f'You rush in and do {player1.melee} damage']))
            monster1.health = monster1.health - player1.melee
            ded_monster()
            if monster1.health <= 0: break
            turn_end()
            continue

        elif action in ['spell', 's']:
            print(random.choice([f'You cast a fireball from your left nostril and do {player1.spell} damage', f'You wink your eye and do {player1.spell} damage', f'You utter a cutting and witty insult and do {player1.spell} damage']))
            monster1.health = monster1.health - player1.spell
            ded_monster()
            if monster1.health <= 0: break
            turn_end()
            continue

        elif action in ['potion', 'p']:
            player1.health += player1.potion()
            turn_end()
            continue

        elif action in ['run', 'r']:
            print('Um, yeah, you can\'t run.')
            turn_end()
            continue

        elif action == 'k':
            monster1.health -= monster1.health
            ded_monster()
            if monster1.health <= 0: break
            turn_end()

        else:
            print('please enter a valid command')
            input('hit <Enter> to continue')
            continue

        break


# BOARD AND CHARACTER SETUP
width = 10
height = 10
board = []
for i in range(height):
    board.append([])
    for j in range(width):
        board[i].append(' ')

# PLAYER LOCATION ON THE BOARD
player_i = 4
player_j = 4

# 4 RANDOMLY POSITIONED ENEMIES
for i in range(4): #iterating through the board to create enemies
    enemy_i = random.randint(0, height - 1) # creating random coordinate
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

# MOVEMENT AND GAMEPLAY LOOP
while True:
    system('cls')
    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end='  ')  # otherwise print the board square
        print()

    command = input('what is your command? \n> ').lower()  # get the command from the user

    if command in ['quit', 'done', 'exit', 'q', 'x']:
        break  # exit the game
    elif command in ['left', 'west', 'l', 'w']:
        player_j -= 1  # move left
    elif command in ['right', 'east', 'r', 'e']:
        player_j += 1  # move right
    elif command in ['up', 'north', 'u', 'n']:
        player_i -= 1  # move up
    elif command in ['down', 'south', 'd', 's']:
        player_i += 1  # move down
    else:
        print('please enter a valid command')
        input('hit <Enter> to continue')
    if player_i >= 10:
        print('You\'ve hit a bouncy wall!')
        player_i -= 3
        input('hit <Enter> to continue')
    elif player_i < 0:
        print('You\'ve hit a bouncy wall!')
        player_i += 3
        input('hit <Enter> to continue')
    elif player_j >= 10:
        print('You\'ve hit a bouncy wall!')
        player_j -= 3
        input('hit <Enter> to continue')
    elif player_j < 0:
        print('You\'ve hit a bouncy wall!')
        player_j += 3
        input('hit <Enter> to continue')

    # check if the player is on the same space as an enemy and BATTLE!
    if board[player_i][player_j] == '§':
        new_monster_init()
        battle()

    # Health checks and battle count
    if player1.health <= 0 and monster1.health <= 0:
        print('You and the monster have killed each other. What a waste.')
        input('hit <Enter> to continue\n>')
        break
    elif player1.health <= 0:
        ur_ded()
        break
    elif battle_count == 0:
        system('cls')
        print('It looks like you\'ve killed everyone here. You savage!')
        print(r'''   _ /\.'|_
   _.-| |\ | / |_
  / \ _>-"""-._.'|_
 >`-.'         `./ \
/`./             \-<
`-|               |_/
/_|   You  Win    |_\
) |               | |
-<|               |\/
`'_\             /`<
 |_/`.         .'\_/
  \_/ >-.._..-'\_|
    `-`_| \_\|_/
     |   `' |  |
     |      |  |
     |      |  |
     |      |  |
     |      |  |
     |  /\  |  |
     | /| \ |\ |
     |/ |/ \| \| ''')
        input('hit <Enter> to continue\n>')
        system('cls')
        break
