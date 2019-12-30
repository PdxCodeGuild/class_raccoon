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
print("The 10 most common words (besides words like 'the' and 'and') in War and Peace are:")
for i in range(0,10):
    print(words[i])

#Version 2 - 10 most common pairs of words
twopair = []
for x in range(len(text)-1):
    pair = (text[x] + " " + text[x+1])
    twopair.append(pair)

pair_dict = {}
for x in twopair:
    if x in pair_dict:
        pair_dict[x] += 1
    else:
        pair_dict[x] = 1

pairs = list(pair_dict.items())
pairs.sort(key=lambda tup: tup[1], reverse=True)

#get rid of common pairs like "and the"
commonpairs = [pair[0] for pair in pairs]
excludepairs = []

def pair_exclude(bottomrange, toprange):
    for i in range(bottomrange, toprange):
        excludepairs.append(commonpairs[i])
    return excludepairs

excludepairs = pair_exclude(0,7)
excludepairs = pair_exclude(8,9)
excludepairs = pair_exclude(10,23)
excludepairs = pair_exclude(24,31)
excludepairs = pair_exclude(32,35)
excludepairs = pair_exclude(36,39)
excludepairs = pair_exclude(40,44)
excludepairs = pair_exclude(47,53)

pairs = [pair for pair in pairs if pair[0] not in excludepairs]

#display 10 most common pairs
print("The 10 most common pairs of words (besides pairs like 'and the') in War and Peace are:")
for i in range(0,10):
    print(pairs[i])