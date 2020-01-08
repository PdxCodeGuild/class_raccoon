'''
Lab 2: Mad Libs

Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions

Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib
Example:

>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
'''


'''
"Im in a glass case of emotion."
'''

#variables and user input
a = input("\n\nChoose a type of material: ")
b = input("\nAn enclosed space: ")
c = input("\nA mental state: ")

print(f"\n\n\nI am in a {a} {b} of {c}!!!")
