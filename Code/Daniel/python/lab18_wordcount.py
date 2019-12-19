import requests
import string
import re


text_dict = {}

response = requests.get("http://www.gutenberg.org/cache/epub/19942/pg19942.txt")
text = response.text.lower()
text = re.findall(r"\w+'*\w+", text)

for word in text:
    if word in text_dict:
        text_dict[word] +=1
    else:
        text_dict[word] = 1
words = list(text_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(10,min(20, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
