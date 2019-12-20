'''
Filename: lab19_ari.py
Author: Dylan
Purpose: Calculate ARI of different texts. 
'''

#mods
import requests
import re
import random
import get_random_text

#variables
code = get_random_text.get_random_book_code()
title = get_random_text.get_book_title(code)
text = get_random_text.get_book_text(code)
text_list = text.split(" ")
text_list_nopunct = re.findall(r'\w+', text)
num_of_words = len(text_list)
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


#methods
def get_num_of_chars(text_list):
    num_of_chars = 0
    for word in text_list_nopunct:
        for char in word:
            num_of_chars += 1
    return num_of_chars

def get_num_of_sentences(text):
    period_count = 0 
    skip_words = ["mr.","mrs.","ms.","esq.","ph.d.","dr.","st.","rd.","ave.","a.d","b.c","e.g.","i.e.","etc."]
    for punct_word in text_list:
        if punct_word.lower() in skip_words:
            continue
        elif "." in punct_word:
            period_count += 1
    return period_count

def get_score():
    sent_count = get_num_of_sentences(text_list)
    char_count = get_num_of_chars(text_list_nopunct)
    score = 4.71 * (char_count / num_of_words) + 0.5 * (num_of_words / sent_count) - 21.43
    return round(score)

def output_ari_score():
    score = get_score()
    if score > 14:
        score = 14
    print(f"This book has an ARI score of {score}")
    print(f"That means is is best for students aged, {ari_scale[score]['ages']},")
    print(f"And is meant for grade level: {ari_scale[score]['grade_level']}")

if __name__ == "__main__":
    print(f"The book is: {title}")
    output_ari_score()