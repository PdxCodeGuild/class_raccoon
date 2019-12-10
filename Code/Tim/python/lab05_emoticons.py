import random
import os

horizontal_eyes = ["8", "%", "B", ";", ":"]
horizontal_noses = ["-", "^", ""]
horizontal_mouths = ["O", "*", "(", ")", "|"]

vertical_eyes = ["+", "*", "@", "☉", "ၜ", "စ", "Ꙩ" ]
vertical_noses = [".", "ϖ", "ပ"]

style = int(input("Would you like a (1) horizontal emoticon or a (2) vertical emoticon? "))
os.system("cls")

if style == 1:
    print("Here you go!\n\n\n\n")
    print(random.choice(horizontal_eyes) + random.choice(horizontal_noses) + random.choice(horizontal_mouths), "\n\n\n")
elif style == 2:
    print("Here you go!\n\n\n\n")
    print(random.choice(vertical_eyes) + random.choice(vertical_noses) + random.choice(vertical_noses))
