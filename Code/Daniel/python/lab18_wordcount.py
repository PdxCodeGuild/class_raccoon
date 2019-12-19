import requests
import string
import re


text_dict = {}
doubles_dict = {}
choice_dict = {}
user_choice = input("What word would you like to start with? ").lower()

response = requests.get("http://www.gutenberg.org/cache/epub/19942/pg19942.txt")
text = response.text.lower()
words = re.findall(r"\w+'*\w+", text)

for word in words:
    if word in text_dict:
        text_dict[word] +=1
    else:
        text_dict[word] = 1
output_words = list(text_dict.items()) # .items() returns a list of tuples
output_words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(output_words))):  # print the top 10 words, or all of them, whichever is smaller
    print(output_words[i])
    



# build a list of tuples [('I', 'ran'), ('ran', 'to'), ('to', 'the')]
word_pairs = []
for i in range(len(words )-1):
    pair = (words[i], words[i+1])
    word_pairs.append(pair)
for pair in word_pairs:
    if pair in doubles_dict:
        doubles_dict[pair] += 1
        # print("added pair")
    else:
        doubles_dict[pair] = 1
        # print("new pair")
output_pairs = list(doubles_dict.items())
output_pairs.sort(key=lambda  tup: tup[1], reverse=True)
for i in range(min(10, len(output_pairs))):
    print(output_pairs[i])

choice_pair = []

for pair in word_pairs:
    if user_choice == pair[0]:
        choice_pair.append(pair)
for pair in choice_pair:
    if pair in choice_dict:
        choice_dict[pair] += 1
    else:
        choice_dict[pair] = 1
choice_output = list(choice_dict.items())
choice_output.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(choice_output))):
    print(choice_output[i])


