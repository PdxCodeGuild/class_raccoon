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
'''

import random
eyes = [':', 'B', '8', ';', 'x', 'X']
noses = ['-', '>', '%']
mouths = [')', 'D', 'p', '(', '3', 'P', '*', '^', 'v', 'V', 'd', '[', ']', '{', '}', '"', 'c', 'C', 'o', 'O', '0', '/', '\\']
print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
