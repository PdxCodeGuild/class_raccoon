from secrets import hp_key
import requests
import json
import string
import random
from os import system

#Pulling the info from the API
url = 'https://www.potterapi.com/v1/'
characters = requests.get(url+'characters', params=hp_key)
char_data = json.loads(characters.text)
spells = requests.get(url+'spells', params=hp_key)
spell_data = json.loads(spells.text)

def housecheck(char_data):
    house = input('What Hogwarts house would you like to choose? (Gryffindor, Hufflepuff, Ravenclaw, Slytherin)\n> ')
    for i in range(len(char_data)):
        try:
            if char_data[i]['house'] == house.title():
                print(char_data[i]['name']+', ', end='')
        except KeyError:
            continue

def wandgetter(character):
    wand = ' '
    for i in range(len(char_data)):
        try:
            if char_data[i]['name'] == character.title():
                if wand == 'None' or wand == None:
                    continue
                wand = char_data[i]['wand']
                return wand
        except KeyError:
            continue

def randspell(spell_data):

    print('\nAnd here\'s a random spell they might perform: \n')
    spell_index = random.choice(range(len(spell_data)))
    print(spell_data[spell_index]['spell'], '\nWhich', spell_data[spell_index]['effect']+'\n')

system('cls')

housecheck(char_data)
character = input('\nFrom the characters above, pick one.\n> ')
wand = wandgetter(character)
system('cls')
if wand is not ' ' and wand is not None:
    print(f'\n{character.title()}\'s wand is {wand}.')
elif wand is None:
    print(f'\nWe don\'t know what kind of wand {character.title()} uses.')
randspell(spell_data)
print('Thank you for using this incredibly useful program. Bye.\n\n')
