'''
Filename: lab18_count_words.py
Author: Dylan
Purpose: Output various breakdowns of text from eBook. 
'''

#mods
import helper
import requests
import re
import random

#methods


#ok, I wasn't making methods before because, well I guess I thought it'd only be like 10 lines of code.
#but I'll do that now. 
 
def pair_dict(word_list):
    new_dict = {}
    for i in range(len(word_list)-1):
        if f'{word_list[i]} {word_list[i+1]}' not in new_dict:
            new_dict[f'{word_list[i]} {word_list[i+1]}'] = 1
        else:
            new_dict[f'{word_list[i]} {word_list[i+1]}'] += 1
    return new_dict

def count_dict(words):
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts

def ordered_tuples(dictionary): 
    dict_tupes = list(dictionary.items())
    dict_tupes.sort(key = lambda tup: tup[1], reverse=True)
    return dict_tupes

    
def print_top_ten():
    for i in range(min(10, len(ordered_pairs))):  # print the top 10 words, or all of them, whichever is smaller
        print(ordered_pairs[i])

def make_following_dict(ordered_pairs):
    counted_dict = {}
    for pair in ordered_pairs:
        pair_words_list = pair[0].split()
        word_count = pair[1]
        first_word = pair_words_list[0]
        second_word = pair_words_list[1]
        if first_word in counted_dict:
            for x in range(word_count):
                counted_dict[first_word].append(second_word)
 
        else:
            counted_dict[first_word] = []
            for x in range(word_count):
                counted_dict[first_word].append(second_word)
    return counted_dict

def print_following_random(word,counted_dict):
    i = 0
    while i < 10:
        following_words_list = counted_dict[word]
        following_word = random.choice(following_words_list)
        print(f"{word.capitalize()} => {following_word.capitalize()}")
        word = following_word
        i += 1
        
        

'''
{
    'of': ['the', 'the', 'the', 'his']    #create this data structure to randomly select the words that most frequently follow

}'''
def print_input_pairs(word, ordered_pairs):
    i = 0
    while i < 10:
        for pair in ordered_pairs:
            pair_words_list = pair[0].split()
            first_word = pair_words_list[0]
            second_word = pair_words_list[1]
            if word.lower() == first_word.lower():
                print(pair)
                word = second_word
                i += 1
                break

response = requests.get('http://textfiles.com/etext/NONFICTION/epicurus-principal-749.txt', headers={'User-Agent': 'Mozilla/5.0'})
text = response.text
text_list = re.findall(r'\w+', text)
text_nopunct = [word for word in text_list if word.isalpha()]
pair_counts = pair_dict(text_nopunct)
ordered_pairs = ordered_tuples(pair_counts)
dict_of_succeding_words = {}

if __name__ == "__main__":
    print("This program will select a word that commonly follows the entry word, and then select one following that. \nPlease enter the word to search for.")
    search_word = helper.text_checker(input("> "), text_nopunct)
    #print_input_pairs(search_word,ordered_pairs)
    counted_dict = make_following_dict(ordered_pairs)
    print_following_random(search_word, counted_dict)
