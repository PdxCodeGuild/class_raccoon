

import requests

text = 'hello world goodbye world apple apple banana apple'

response = requests.get('http://textfiles.com/etext/FICTION/7gabl10.txt')
text = response.text

word_dict = {
    'hello': 1,
    'world': 2,
    'goodbye': 1,
    'apple': 3,
    'banana': 1
}

def add(a, b):
    return a + b
add = lambda a, b: a + b



words = list(word_dict.items()) # .items() returns a list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])