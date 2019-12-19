#lab18_countwords.py

import requests
import string
import re

punct = string.punctuation
punct = [c for c in punct if c != "'"]
punct = "".join(punct)

wnp = requests.get('http://www.gutenberg.org/files/2600/2600-0.txt')
text = (wnp.text).lower()
text = re.findall(r"\w+'*\w+", text)

word_dict = {}
for x in text:
    if x in word_dict:
        word_dict[x] += 1
    else:
        word_dict[x] = 1

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)

#get rid of common words like the and is
commonwords = [word[0] for word in words]
excludewords = []

def exclude(bottomrange, toprange):
    for i in range(bottomrange, toprange):
        excludewords.append(commonwords[i])
    return excludewords

excludewords = exclude(0,37)
excludewords = exclude(39,57)
excludewords = exclude(59,64)
excludewords = exclude(65,71)
excludewords = exclude(75,79)

words = [word for word in words if word[0] not in excludewords]

#display 10 most frequent uncommon words
for i in range(0,10):
    print(words[i])
