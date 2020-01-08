'''
Lab 18: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values.
If a word isn't in your dictionary yet, add it with a count of 1.
If it is, increment its count.
Print the most frequent top 10 out with their counts.
You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
'''

import requests #Requests is an Apache2 Licensed HTTP library, written in Python. It is designed to be used by humans to interact with the language. This means you don’t have to manually add query strings to URLs, or form-encode your POST data.

#What can Requests do?

#Requests will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way.


import re#A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory.

#The concept arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language. The concept came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax.

#Regular expressions are used in search engines, search and replace dialogs of word processors and text editors, in text processing utilities such as sed and AWK and in lexical analysis. Many programming languages provide regex capabilities either built-in or via libraries.

response = requests.get('http://textfiles.com/etext/FICTION/sister_carrie')#getting a response from the url. using the requests library.
text = response.text#because we only want the text from the response
text = re.findall(r"\w+'*\w+", text)#this finds each individual word in the text. \w is a single digit word. + means the single character word plus more characters. ' means its including words with apostrophes. the * means there could be a word without an apostrophe but if it does have an apostrophe we add the other \w+ or length of second part of word.

word_dict = {}#we will be filling this dictionary with code from below

for word in text: #for any word in the list of text. ".findall" creates a list
    if word in word_dict: #if word is in dictionary
        word_dict[word] += 1 #each time the word occurs it adds a value of 1 to the dict
    else:
        word_dict[word] = 1 #if the word only occurs once

# word_dict is now a dictionary where the key is the word and the value is the count

words = list(word_dict.items())# .items() is a method used with dictionaries that returns a list of tuples from said dictionary. so now we have a list of key:value pairs.
words.sort(key=lambda tup: tup[1], reverse=True)# sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
