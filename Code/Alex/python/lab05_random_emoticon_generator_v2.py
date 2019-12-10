'''
Lab 5: Random Emoticon Generator

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
Example output:

:-P

Version 2
Use a while loop to generate 5 emoticons.

#advanced 1 example
out_str = ''
for num_var in range(0, 5): #0, 1, 2, 3, 4
    out_str = out_str + random.choice(notes)
    out_str = out_str + ' '
    print(out_str)

( ͡° ͜ʖ ͡°)
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
i = 0


#calculating to make it random and to print it 5 times
while i < 5:
    i += 1
    print(random.choice(left_side_of_face) + random.choice(left_eye) + random.choice(mouth) + random.choice(right_eye) + random.choice(right_side_of_face))


#ignore
'''
out_str = ''
for combo_var in range(0, 5):
    out_str = out_str + (random.choice(eyes) + random.choice(noses) + random.choice(mouths))
    out_str = out_str + ' '
print(out_str)
'''
