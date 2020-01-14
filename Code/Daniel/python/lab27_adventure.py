import random
from os import system, name 
from time import sleep 

width = 20  # the width of the board
height = 20  # the height of the board

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


class birb: # bird classes and parameters
    def __init__(self, bird, hp, name, atk, icon):
        self.bird = bird
        self.hp = hp
        self.name = name
        self.atk = atk
        self.icon = icon
        self.i_pos = random.randint(0, height - 1)
        self.j_pos = random.randint(0, width - 1)

    def __str__(self):
        return(self.bird)
    
    def move(self): # making the birds move some
        moves = ["w","a","s","d","none"]
        
        choice = random.choice(moves)

        if choice == "a":
            if self.j_pos != 0:
                self.j_pos -= 1  # move left
            elif self.j_pos == 0:
                self.j_pos += width-1 # loop back to the right side of the map
        elif choice == "d":
            if self.j_pos != width-1:
                self.j_pos += 1  # move right
            elif self.j_pos == width-1:
                self.j_pos -= width-1 # loop back to the left
        elif choice == "w":
            if self.i_pos != 0:
                self.i_pos -= 1  # move up
            elif self.i_pos == 0:
                self.i_pos += height-1 # loop to the bottom
        elif choice == "s":
            if self.i_pos != height-1:
                self.i_pos += 1  # move down
            elif self.i_pos == height-1:
                self.i_pos -= height-1 # loop to the top
        


# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


clear()




for i in range(2):
    fruit_i = random.randint(0, height - 1)
    fruit_j = random.randint(0, width - 1)
    board[fruit_i][fruit_j] = '♥'



# adding enemy images

bird_1 ='''     .   ,
            '. '.  \  \\
           ._ '-.'. `\  \\
             '-._; .'; `-.'. 
            `~-.; '.       '.
             '--,`           '.
                -='.          ;
      .--=~~=-,    -.;        ;
      .-=`;    `~,_.;        /
     `  ,-`'    .-;         |
        .-~`.    .;         ;
         .;.-   .-;         ,\\
           `.'   ,=;     .-'  `~.-._
            .';   .';  .'      .'   '-.
              .\  ;  ;        ,.' _  a',
             .'~";-`   ;      ;"~` `'-=.)
           .' .'   . _;  ;',  ;
           '-.._`~`.'  \  ; ; :
                `~'    _'\\_ \\_ 
                      /=`^^=`""/`)-.
                      \ =  _ =     =\\
                       `""` `~-. =   ; '''


bird_2 ='''          \\| , \\,/ .|/, .
                \|`@,"@,@`,@",@`@,@,\/_
             _\\`@,"@,"@,"@`@,"@",@`@,"@",|_
            \\,"@",@`@,"@,"@",@`,@",@`@",@"@/_
         _\\,"@`@,"@",@,"@",@`@,'@",@,"@`@",`@/,
        \\|,@`@,",@'@",@",@",@`@",@,"@,@,@`@,"@`<
       >,"@",@",@`",@",@",@`@",@",@,'@,"@,"@,"@,/_
     _\\,"@`@,"@",@`@",@"@,`@,\\!/@,"@,`@",@",@",@`
       @,"@"@,`@",@,"@,@",@",\\W/,@",@`@",@",@`,@,/_
     \\`@",@`,"@`@,"@,`@,@`,@/ a_\\`@","@","@,`@"@,`
     /,@`@,"@`@,"@,"@",",`@,| (`@",",@",`@`@",",@_
     _'@,'@,"@,"@`,","@`,"'-' |",`@",@",",`@",`@\\
      /`@`,@,"@,'@`@,"@,"=    |@",@`@",@`@",@`@<
      >.@',@","@,"@,","@/,___/ `@,",`@",@",`@"_`
       /,"@."@'@,"@`,"  /  |      `@",`@",`@",\\
        /,@`@`,",@"   _| _|        ` "`@",<-
           /|`/`        /\\ /\\            `\\
 
'''

bird_3 =''' 
.--._
             '. ='-._
               '.= =('-.
                 \\ = (( '.
          ,       | =((  _\\.___
         /=`"--.,_;..--'`     _`'.
        /  =      .------.   (o) )>
       /_=___,.../= `((   |_.--'`
              _.'  = ((   /
         _.-'`=  = _((   /
      .-'__=___=___((_,.'
'''

bird_4 ='''
           .:%@&'@&:.                  .::&@&'&::.
         .::&@.&@:'                  '::&.@&@'
       ':: @.&@:'                  .:@&.@'___
          .::@&::'                  '_.:-'   `',
        ':&.@&@:.               _.-''      _.-'
         .:&@&::.        ____.-'       _.-:.
        .&'@@.&@'      .::.-.\\     _.-'@&@:'
         '::@&@::.    /;:/(o)\\_.-'  '&@.&@:.
         .:@'&&::.   |;:;:---' \\```\'''---.._`
        .: :&&@: .   /;:;'     /`'----------`     
         ':&.@&:'   /;;;      |     .::@&@&::'
        .:@&.@&._._/:;;       |     .:&'@@:.
        ':.=####=#.:;:;       |   ': @&.@ :'.
         /#/##/###\\;;:;;.     /    .:@.&@::.
        /#/#/##/##/;:;:;:'  .'      .:&@&::'
       //##/#/##/##|:::;;.-'       ': @&@.&:'
      /#/##/##/##/;:;;;:;/        .::@'&@& : '
     |#/##/#/##/##/;:;:/`. .   ': .@&@'&@::'
     '-#/##/##/#/:\\\\=\\\\.:.'::@&@'&@&.@::.
        /##/##;;//))) /)))@&.@&@'&@&.@&::'
       /;;;/;/:/'&@.&@&@.&@&@'@& @&::.
      /;:/;:--'@&@'&&.&@&@&.@&&'@::'.
     /;/;;:| `::' '::@:' @&::' . ' 
    /;::/:;|      '  ''  ` '
   |;/:::;/
   \\;:;/;/
    `"""`
'''
heart = ''' 
             \\ \\ | |/ /
             |\\ `' ' /
             ;'      \\      / ,
            ;    _,   |    / / ,  
            |   (  `-.;_,-' '-' ,
            `,   `-._       _,-'_
           ,-`.    `.)    ,<_,-'_, 
         ,'    `.   /   ,'  `;-' _,  
        ;        `./   /`,    \\-'
        |         /   |  ;\\   |\\
        |        ;_,._|_,  `, ' \\
        |        \\    \\ `       `,
        `      __ `    \\         ;,
         \\   ,'  `      \\,       ;;
          \\_(            ;,      ;;
             \\           `;,     ;;
              `.          `;;,   ;'
                `-.        ;;;;,;'
                   `-.._  ,;;;;;'
                        ``';;;'  
'''

enemy_birb1 = birb(bird_1, 56, "Ameribirb", 10, "Ϫ")
enemy_birb2 = birb(bird_2, 30, "The Birbzerker", 15, "Ϫ")
enemy_birb3 = birb(bird_3, 15, "Smolbirb", 5, "Ϫ")
enemy_birb4 = birb(bird_4, 70, "Carl", 12, "Ϫ")

player_hp = 100 
enemy_list = [enemy_birb1, enemy_birb2, enemy_birb3, enemy_birb4]  
# loop until the user says 'done' or dies
while True:
    sleep(1)
    clear()

        # print out the board
    for i in range(height):
        for j in range(width):
            for birds in enemy_list:
                if birds.j_pos == j and birds.i_pos == i:
                    print(birds.icon, end = " ")
                # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
            
        print()

    command = input('Move with WASD keys, type quit to quit ').lower()  # get the command from the user

    if command in ['done' , 'quit' , 'end']:
        break  # exit the game
    elif command in ['a']:
        if player_j != 0:
            player_j -= 1  # move left
        elif player_j == 0:
            player_j += width-1 # loop back to the right side of the map
    elif command in ['d']:
        if player_j != width-1:
            player_j += 1  # move right
        elif player_j == width-1:
            player_j -= width-1 # loop back to the left
    elif command in ['w']:
        print(player_i)
        if player_i != 0:
            player_i -= 1  # move up
        elif player_i == 0:
            player_i += height-1 # loop to the bottom
    elif command in ['s']:
        print(player_i)
        if player_i != height-1:
            player_i += 1  # move down
        elif player_i == height-1:
            player_i -= height-1 # loop to the top
    


    
    def_counter = 0 # counter to make defense last for 2 turns, otherwise it would be useless
    player_def = 0 # player defense multiplier
    # enemy_hp = 0
    # check if the player is on the same space as the heart
    if board[player_i][player_j] == '♥':
        clear()
        print(heart)
        heart_choice = input("You've found an actuall human heart on the ground, goss... wanna eat it? ").lower()
        if heart_choice in ["y", "yes"]:
            print("Wow, you actually ate it, you should get help. You gain 15 HP and some severe mental trauma.")
            player_hp += 15
            board[player_i][player_j] = " "
            sleep(3)
        else:
            print("Of course you don't want to eat it, that would be disgusting. However, this is a video game, so it might also give you HP... just saying.")
            board[player_i][player_j] = " "
            sleep(3)
    


    for enemy in enemy_list:
        if player_i == enemy.i_pos and player_j == enemy.j_pos : # if you're sitting on an enemy
            sleep(1)
            clear()
            fight_enemy = enemy
            enemy_hp = enemy.hp
            print(fight_enemy)
            print(f'you\'ve encountered {fight_enemy.name} with {enemy_hp} HP') # telling the player they're sitting on an enemy
            while enemy_hp > 0 or player_hp > 0:
                print(f"Your HP is {player_hp}, enemy HP is {enemy_hp}")
                
                action = input('Would you like to attack or defend?') # ask them what they want to go
                if action == 'attack': # line 185-201 lists all attack outcomes
                    player_atk = random.randint(0,100)
                    if player_atk == 0:
                        print("You grabbed your sword by the pointy bit, lose 10 HP")
                        player_hp -= 10
                    elif 0< player_atk<= 5:
                        print("You managed to hit yourself in the foot, lose 5 HP")
                        player_hp -= 5
                    elif 5<player_atk<50:
                        print(f"You managed to land a hit on {fight_enemy.name}, doing 10 damage")
                        enemy_hp -= 10
                    elif 50<=player_atk<99:
                        print(f"That was quite the swing there bucco, you did 20 damage to {fight_enemy.name}")
                        enemy_hp -= 20
                    elif player_atk == 100:
                        print(f"{fight_enemy.name} is now a fine pink mist, maybe you should calm down a little")
                        enemy_hp -= 100
                
                
                if action == 'defend': # line 203-216 lists all defense outcomes
                    def_counter = 0
                    def_action = random.randint(0,100)
                    if def_action == 0:
                        print(f"You managed to deflect {fight_enemy.name}'s attack directly into your face, good job")
                        if 1 or 2 in def_counter:
                            player_def = -1
                    elif 0<def_action<50:
                        print(f"You managed to get your shield mostly in the way of {fight_enemy.name}'s attack")
                        if 1 or 2 in def_counter:
                            player_def = .5
                    elif 50<=def_action<90:
                        print(f"That wasn't a bad block, your should do that more often")
                        if 1 or 2 in def_counter:
                            player_def = .75
                    elif def_action >= 90:
                        print("You managed to block their attack entirely")
                        if 1 or 2 in def_counter:
                            player_def = 1
            
                
                if enemy_hp <=0:
                    print(f"You have slain the mighty {fight_enemy.name}, your birbslaying adventure continues")   # I wanted to check enemy and player health after
                    enemy_list.remove(enemy)
                    break
                

                # actuall damage is calculated by enemy attack * d100 score value - enemy attack * player defense multiplier
                enemy_atk = random.randint(0,100)
                if enemy_atk == 0:
                    print(f"{fight_enemy.name} missed you completely")
                if 0<enemy_atk<25:
                    print(f"{fight_enemy.name} hit you, but not very hard")
                    enemy_dmg = (fight_enemy.atk*.25) - (fight_enemy.atk*player_def) 
                    if enemy_dmg < 0:
                        enemy_dmg = 0
                    player_hp -= enemy_dmg
                    print(f"You took {enemy_dmg} damage")
                    round(player_hp)
                elif 25<=enemy_atk<75:
                    print(f"{fight_enemy.name} landed a solid hit")
                    enemy_dmg = (fight_enemy.atk*.75) - (fight_enemy.atk*player_def)
                    if enemy_dmg < 0:
                        enemy_dmg = 0
                    player_hp -= enemy_dmg
                    print(f"You took {enemy_dmg} damage")
                    round(player_hp)
                elif 75<=enemy_atk<=99:
                    print(f"{fight_enemy.name} pecked you right in the face, that must have hurt")  
                    enemy_dmg = fight_enemy.atk - (fight_enemy.atk*player_def)
                    if enemy_dmg < 0:
                        enemy_dmg = 0
                    player_hp -= enemy_dmg
                    print(f"You took {enemy_dmg} damage")
                    round(player_hp)
                elif enemy_atk == 100:
                    print(f"{fight_enemy.name} lets out a mighty 'KAW!' and pecks you right in the eye, you should probably go see a doctor")
                    enemy_dmg = fight_enemy.atk*2
                    print(f"You took {enemy_dmg} damage")
                    player_hp -= enemy_dmg
                    round(player_hp)
                def_counter +=1
                if def_counter > 2:
                    def_counter = 0
                # print(def_counter)
                if player_hp <=0:
                    print(f"Your adventure ends here, you were pecked to death by {fight_enemy.name}, good job, you lost to a bird")
                    exit()
    for bird in enemy_list:
        bird.move()
        # print(bird.i_pos)
            
    if enemy_list == []:
        print("You did it, you killed all the adorable birds and irreparably damaged the local ecosystem, good job!")   
        sleep(3)
        clear()
        exit()        
           
            
        
            

       