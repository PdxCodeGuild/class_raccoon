#lab 18 count words Brandon G.

# Version 2
# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

# Version 3 (optional)
# Let the user enter a word, then show the words which most frequently follow it.

import requests
import re

#Fuction for getting a book and finding the words in it.
def create_list():
    etext = requests.get('http://textfiles.com/etext/FICTION/longfellow-paul-210.txt')
    etext = etext.text.lower()
    x = re.findall(r"\w+'*\w+", etext)
    return(x)

#Function for creating a dictionary that includes the word and how many times it appears.   
def etext(x):
    book_dict = {}
    for word in x:
        if word not in book_dict:
            book_dict[word] = 1
        else:
            book_dict[word] += 1
    
    words = list(book_dict.items()) # .items() returns a list of tuples
    new_list = []
    
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        new_list.append(words[i])
    return(new_list)

#Function for finding pairs of words, and how often they occur
def word_pair(x):
    pair_dict = {}
    pair_list = []
    for i in range(len(x)-1):  
        pair_words = x[i], x[i+1]
        pair_list.append(pair_words)
    for pair in pair_list:
        if pair not in pair_dict:
            pair_dict[pair] = 1
        else:
            pair_dict[pair] += 1
    
    words = list(pair_dict.items()) # .items() returns a list of tuples
    
    new_list = []
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        new_list.append(words[i])
    return(new_list)

 




#Function for finding a specific word in the book and how many times it appears.
# def find_word(pick_word):


    
book = create_list()
print(f"This is your 10 most common words in order:\n{etext(book)}")
print("\n")
print(f"This is your 10 most common pairs of words:{word_pair(book)}")
# print("Would you like to find a specific word?")
# while True:
    # pick_word = input("")