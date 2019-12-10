# lab05_emoticon.py
"""
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
"""
# import modules
import random


# define list
eye_var = [":", ";", "X", "="]
nose_var = [">", ".", "", "-"]
mouth_var = ["P", "O", "(", ")", "I"]
output_var = random.choice(eye_var) + random.choice(nose_var) + random.choice(mouth_var)


print(output_var)
