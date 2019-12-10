#Generate emoticons at random
import random
#Variable lists
emoticon_left = ["(", "\(", "¯\_("]
emoticon_right = [")", ")/", ")_/¯", ")╯ ┻━┻"]
emoticon_face = ["o.o", "uwu", "0_0", "O.o", "-_-"]

#random chooser for one face
print("\nHey look, a randomized emoticon, isn't that zany?\n")

print(random.choice(emoticon_left) + random.choice(emoticon_face) + random.choice(emoticon_right))

print("\nOh god, there are more of them, run for your lives!\n")

#random generator for multiple faces
output = ""
for num in range(5):
    output = output + random.choice(emoticon_left) + random.choice(emoticon_face) + random.choice(emoticon_right) + " "
print(f"\n{output}\n")
