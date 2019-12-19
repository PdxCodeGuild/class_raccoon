'''
Lab 18: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency
and display the most frequent words to the user in the terminal.
Remember there isn't any "perfect" way to identify a word in english
(acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase, strip punctuation, split into a list of words.
3. Your dictionary will have words as keys and counts as values.
If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
4. Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

'''
import requests
import re
import string
import operator

# Open the file.
response = requests.get('http://textfiles.com/etext/MODERN/agrippa.txt')
text = response.text

# Make everything lowercase, strip punctuation, split into a list of words.
text = text.lower()

# Find all the texts
text = re.findall(r"\w+'*\w+", text)

# Creats an empty dictionary
dict = {}

# Dictionary will have words as keys and counts as values.
# Count the words in text by loop though
for word in text:
    # if word in dictionary
    if word in dict:
        # increment its count
        dict[word] += 1
    # if word not in exist in dictionaty
    else:
        # add it with a count of 1.
        dict[word] = 1

# sort largest to smallest, based on count

# .items() returns a list of tuples
words = list(dict.items())

# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)

# print the top 10 words, or all of them, whichever is smaller
for i in range(min(10, len(words))):
    print(words[i])
