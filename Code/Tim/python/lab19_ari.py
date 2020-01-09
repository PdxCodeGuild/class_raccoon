import requests
import string
import collections
import re

# Pulling source text from website and setting up variables
response = requests.get('http://textfiles.com/etext/AUTHORS/PLATO/plato-crito-340.txt')
text = response.text
words = 0
chars = 0
sentences = 0

def word_counter(x):
    global words
    count = 0
    for i in re.findall(r'\w+', x):
        count += 1
    words = count

def char_counter(x):
    global chars
    count = 0
    for i in re.findall(r'\w', x):
        count += 1
    chars = count

def sentence_counter(x):
    global sentences
    count = 0
    for i in re.findall(r'\b((?!=|\.).)+(.)\b', x):
            count += 1
    sentences = count



word_counter(text)
char_counter(text)
sentence_counter(text)
print(words)
print(chars)
print(f'words divided by chars = {chars/words}')

ari = (4.71 * (chars/words)) + (0.5 * (words/sentences)) - 21.43
print(f'The ARI of your book is {ari}')
