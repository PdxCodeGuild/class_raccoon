
import requests
import re
import string
import random


url = 'http://textfiles.com/etext/FICTION/longfellow-paul-210.txt'
# url = 'http://textfiles.com/etext/FICTION/7gabl10.txt'
response = requests.get(url)

text = response.text

# word_dict = {
#     'hello': 1,
#     'world': 2,
#     'goodbye': 1,
#     'apple': 3,
#     'banana': 1
# }

# def add(a, b):
#     return a + b
# add = lambda a, b: a + b

text = text.lower()
for punctuation in string.punctuation:
    text = text.replace(punctuation, ' ')
words = text.split()
# # words = [word.lower() for word in words]
# # words = [word.strip(string.punctuation) for word in words]
# # print(words)

# words = re.findall('\w+', text)
# print(words)
# print(len(words))


pairs = []
for i in range(len(words)-1):
    pairs.append((words[i], words[i+1]))

pairs_dict = {}
for pair in pairs:
    first_word = pair[0]
    second_word = pair[1]
    if first_word in pairs_dict:
        pairs_dict[first_word].append(second_word)
    else:
        pairs_dict[first_word] = [second_word]

# for key in pairs_dict:
#     print(key, pairs_dict[key])


starting_word = random.choice(words)
for i in range(100):
    print(starting_word, end=' ')
    next_word = random.choice(pairs_dict[starting_word])
    # print(next_word, end=' ')
    starting_word = next_word


# words = list(word_dict.items()) # .items() returns a list of tuples
# print(words)
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])