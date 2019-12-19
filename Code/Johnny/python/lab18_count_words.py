import requests
import string
import re

# Book to pull
word_dict = {}
response = requests.get("http://www.gutenberg.org/cache/epub/24117/pg24117.txt")
words = response.text.lower()
words = re.findall(r"\w+'*\w+", words)

# for loop for dictionary, if not in dict, it adds the word and continues count
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

out_words = list(word_dict.items()) # .items() returns a list of tuples
out_words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(out_words))):  # print the top 10 words, or all of them, whichever is smaller
    print(f'This is your most common words: {out_words[i]}')


word_pairs = []
for i in range(len(words)-1):
    pairs = (words[i], words[i+1])
    word_pairs.append(pairs)
pairs_dict = {}
for word in word_pairs:
    if word in pairs_dict:
        pairs_dict[word] += 1
    else:
        pairs_dict[word] = 1
out_pairs = list(pairs_dict.items())
out_pairs.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(out_pairs))):
     print(f'This is the most common pairs: {out_pairs[i]}') # prints out most common pairs
