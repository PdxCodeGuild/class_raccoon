import os

#Major keys
c_maj = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
cs_maj = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
d_maj = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
eb_maj = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']
e_maj = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
f_maj = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E' ]
fs_maj = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#',]
gb_maj = ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F',]
g_maj = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
ab_maj = ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
a_maj = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
bb_maj = ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']
h_maj = ['B', 'C#', 'D#', 'E#','F#', 'G#', 'A#']

os.system('cls')

# get input type and validate
while True:
    print('*'*10)
    note_system = int(input('What notation system are you using? (1) Standard letter notation (Gm, C7, F, etc) (2) Roman numeral notation (ii, V7, I) (3) Nashville notation (2, 5, 1)\n> '))
    if note_system not in range(0,4):
        print('Not a valid entry. Please choose 1, 2, or 3.')
        continue
    else:
        os.system('cls')
        break

# get modality
while True:
    tonality = int(input('(1) Major (2) Minor\n> '))
    if tonality != 1 and tonality != 2:
        print('Not a valid entry. Please choose 1 or 2.')
        continue
    else:
        os.system('cls')
        break

# get output type and validate
while True:
    note_system_output = int(input('What notation system do you want to convert to? (1) Standard letter notation (Gm, C7, F, etc) (2) Roman numeral notation (ii, V7, I) (3) Nashville notation (2, 5, 1)\n> '))
    if note_system_output not in range(0,4):
        print('Not a valid entry. Please choose 1, 2, or 3.')
        continue
    else:
        os.system('cls')
        break

chord_list = []

transpose = input('Do you want to transpose? (y/n)\n> ')
