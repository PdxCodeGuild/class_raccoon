

import random


def random_emoticon():
    eyes = [':', ';', '=', '8', 'B']
    noses = ['-', '^', '', ' ', '°']
    mouths = [')', '(', 'D', 'P', 'O', '/', ']', '[', '{', '3']
    return random.choice(eyes) + random.choice(noses) + random.choice(mouths)



print(random_emoticon())




