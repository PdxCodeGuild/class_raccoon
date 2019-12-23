'''*not complete*
Lab 18: Count Words


Version 2

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.
'''

import requests
import re

response = requests.get('http://textfiles.com/etext/FICTION/sister_carrie')
text = response.text
text = re.findall(r"\w+'*\w+", text)

word_dict = {}

for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
