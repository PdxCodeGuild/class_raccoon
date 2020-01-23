import random
import string

def passgen(caps, lower, punc, numbers):
    try:
        caps = int(caps)
        lower = int(lower)
        punc = int(punc)
        numbers = int(numbers)
        if caps < 0 or lower < 0 or punc < 0 or numbers < 0 or numbers+caps+lower+punc == 0:
            return None
        output= []
        upperlist = string.ascii_uppercase
        lowerlist = string.ascii_lowercase
        punclist = string.punctuation
        for i in range(caps):
            output.append(random.choice(upperlist))
        for i in range(lower):
            output.append(random.choice(lowerlist))
        for i in range(punc):
            output.append(random.choice(punclist))
        for i in range(numbers):
            output.append(str(random.randint(1,9)))
        random.shuffle(output)
        return "".join(output)
    except ValueError:
        return None
