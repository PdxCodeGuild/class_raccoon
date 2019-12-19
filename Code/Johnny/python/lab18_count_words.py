import requests
import string
import re

# The war of the worlds
word_dict = {}
response = requests.get("http://www.gutenberg.org/files/36/36-0.txt")
text = response.text.lower()
text = re.findall(r"\w+'*\w+", text)


for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
