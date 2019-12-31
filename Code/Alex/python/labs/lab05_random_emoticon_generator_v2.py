'''
Lab 5: Random Emoticon Generator

Version 2
Use a while loop to generate 5 emoticons.

#advanced 1 example
out_str = ''
for num_var in range(0, 5): #0, 1, 2, 3, 4
    out_str = out_str + random.choice(notes)
    out_str = out_str + ' '
    print(out_str)
'''


#modules
import random

#variables/emoticon expressions
left_side_of_face = ['(', '{', '[', '<', '//', ' ', '']
left_eye = ['o', 'O', '>', 'v', 'V', ' ͡°', "'", '~', '-', '=', '+', '--', 'T', 'p', ' ']
mouth = [' ͜ʖ', '_', ',', 'o', 'O', 'ω', '▽', '.', '', ' ']
right_eye = ['o', 'O', '<', 'v', 'V', ' ͡°', '~', "'", '-', '=', '+', '--', 'T', 'q', ' ']
right_side_of_face = [')', '}', ']', '>', '\\\\', '']
#probably too many choices, but whatever

#variable for calculation purposes
counter = 0
#calculating to make it random and to print it 5 times
while counter < 5:
    counter += 1
    print(random.choice(left_side_of_face) + random.choice(left_eye) + random.choice(mouth) + random.choice(right_eye) + random.choice(right_side_of_face))
