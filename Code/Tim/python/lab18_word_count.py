import requests
import string
import collections
import re

# Pulling source text from website and setting up variables
response = requests.get('http://textfiles.com/etext/AUTHORS/PLATO/plato-crito-340.txt')
text = response.text
small_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she']
text_stripped = ''
word_list = []
word_dict = {}

word_list = re.findall(r'\w+', text)

# Function to strip out the punctuation
def text_stripper(x):
    global text_stripped
    for char in x:
        if char not in string.punctuation:
            text_stripped.append(char)
    return text_stripped

# Function to break the string into a list
# def convert_to_list(text):
#     global word_list
#     word_list = list(text_stripped.split(" "))

# Function to strip out common English words
# def strip_common(text):
#     global word_list
#     global small_words
#     dump = []
#     for word in text:
#         if word_list not in small_words:
#             dump += word
#     word_list = dump

# Function to create the dictionary
def dictionary_maker(listed_text):
    global word_list
    global word_dict
    word_dict = collections.Counter(word_list)

words = list(word_dict.items()) # .items() returns a list of tuples

# text_stripper(text)
# convert_to_list(text_stripped)
#strip_common(word_list) #- doesn't work yet
dictionary_maker(word_list)
words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
# print(word_dict)
print(text_stripped)
