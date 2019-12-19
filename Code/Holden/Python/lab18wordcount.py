import requests
import re

response = requests.get('http://textfiles.com/etext/FICTION/2city11.txt')
text = (response.text).lower()
wordlist = re.findall(r'\w+\'*\w*', text)
word_dict= {}
for word in wordlist:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
word_order = {}
for i in range(len(wordlist)-1):
    if wordlist[i] + ' ' + wordlist[i+1] not in word_order:
        word_order[wordlist[i] + ' ' + wordlist[i+1]] = 1
    else:
        word_order[wordlist[i] + ' ' + wordlist[i+1]] += 1

def print_word_count(word_dict):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
print_word_count(word_dict)
print("list of common pairs of words")
print_word_count(word_order)
while True:
    userword=input('input a word you want to find the most common following words for: ')
    if userword in wordlist:
        break
    print('That word (or nonword input) is not in the text.')
word_follow={}
for i in range(len(wordlist)-1):
    if wordlist[i] == userword and wordlist[i+1] not in word_follow:
        word_follow[wordlist[i+1]] = 1
    if wordlist[i] == userword:
        word_follow[wordlist[i+1]] += 1
print_word_count(word_follow)
