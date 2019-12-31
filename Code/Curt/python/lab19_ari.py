#lab19_ari.py

import requests
import re
import random
import math

def get_random_book_code():
    response = requests.get('https://www.gutenberg.org/ebooks/search/?sort_order=random')
    text = response.text
    # print(text)
    codes = re.findall('/ebooks/(\d+)', text)
    return random.choice(codes)
    # return random.choice(urls)

# https://www.gutenberg.org/files/58714/58714-0.txt
# http://www.gutenberg.org/cache/epub/5785/pg5785.txt
def get_random_book_text():

    code = get_random_book_code()

    url = f'https://www.gutenberg.org/files/{code}/{code}-0.txt'
    response = requests.get(url)
    if response.status_code == 404:
        url = f'http://www.gutenberg.org/cache/epub/{code}/pg{code}.txt'
        response = requests.get(url)
    if "Title: " in response.text: #Attempt to get the title from Project Gutenberg
        title = re.findall(r'Title:\s+(.*)', response.text)
        title = [i.strip() for i in title] #Get rid of the carriage return
        title = ''.join(title)
    else:
        title = "this book"
    return response.text, title

book, title = get_random_book_text()

def counts(book):
    text = book
    charcount = len(re.findall(r"\w", text))
    wordcount = len(re.findall(r"\w+'*\w+", text))
    sentcount = len(re.findall(r"[A-Z].*?[\.!?]", text))

    return charcount, wordcount, sentcount

characters, words, sentences = counts(book)

#get ARI value
ari = (4.71 * (characters/words)) + (0.5 * (words/sentences)) - 21.43
ari = math.ceil(ari)
if ari > 14:
    ari = 14

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

print("--------------------------------------------------------\n")
print(f"The ARI for {title} is {ari}")
print(f"This corresponds to a(n) {ari_scale[ari]['grade_level']} level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.\n")
print("--------------------------------------------------------")
