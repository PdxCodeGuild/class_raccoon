#Lab 19 ARI Brandon G. 
import requests
import re
import random



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




def get_random_book_code():
    response = requests.get('https://www.gutenberg.org/ebooks/search/?sort_order=random')
    text = response.text
    codes = re.findall('/ebooks/(\d+)', text)
    return random.choice(codes)
    
def get_random_book_text():

    code = get_random_book_code()

    url = f'https://www.gutenberg.org/files/{code}/{code}-0.txt'
    response = requests.get(url)
    if response.status_code == 404:
        url = f'http://www.gutenberg.org/cache/epub/{code}/pg{code}.txt'
        response = requests.get(url)

    return response.text

def get_char_count(text):
    char_count = len(re.findall(r"\w",text))
    return char_count
    
def get_word_count(text):   
    word_count = len(re.findall(r"\w*'?\w*",text))
    return word_count

def get_sentence_count(text):
    sentence_count = len(re.findall(r"\s+[^.!?]*[.?!]",text))
    return sentence_count

def get_ari_rating(char,word,sent):
    char = float(char)
    word = float(word)
    sent = float(sent)
    ari_rating = 4.71*(char/word)+.5*(word/sent)-21.43
    print(ari_rating)
    rounded = ari_rating // 1 + 1
    rounded = int(rounded)
    print(rounded)
    if rounded >= 14:
        rounded = 14
    return rounded


# variables assigned run functions
text = get_random_book_text()
char_count = get_char_count(text)
word_count = get_word_count(text)
sentence_count = get_sentence_count(text)
ari_rating = get_ari_rating(char_count,word_count,sentence_count)

# main program 
print (f"The number of characters is: {char_count}")
print (f"The number of words is: {word_count}")
print (f"The number of sentences is: {sentence_count}")
print (f"The ARI level for this book is {ari_rating}")
print (f" {ari_scale[ari_rating]}")