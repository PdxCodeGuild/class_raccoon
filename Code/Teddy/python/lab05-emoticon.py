# Lab 5: Random Emoticon Generator
import random

# Define a list of eyes
eyes_list = [":", ";", "$", "8", "X", "3"]
# Define a list of noses
noses_list = ["-", "+", "{"]
# Define a list of mouths
mouths_list = ["P", "D", ")", "O", "("]

#Generate 5 emoticons
for i in range(5):
    # # Randomly pick a set of eyes
    random_eye = random.choice(eyes_list)
    # Randomly pick a nose
    random_nose = random.choice(noses_list)
    # Randomly pick a mouth
    random_mouth = random.choice(mouths_list)
    # Assemble and display the emoticon
    print(f'{random_eye}{random_nose}{random_mouth}', end = ' ')
print()
