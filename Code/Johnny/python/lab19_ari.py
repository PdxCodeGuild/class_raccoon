
import requests
import re
import random
import math

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
    return response.text

# assigning book to get_random_book_text function to get book if printed
book = get_random_book_text()
text = book
all_chars = len(re.findall(r"\w", text))
all_words = len(re.findall(r"\w+'*\w+", text))
all_sentences = len(re.findall(r"[A-Z].*?[\.!?]", text))
# print(all_chars)
# print(all_words)
# print(all_sentences)

ari = (4.71 * (all_chars/all_words) + 0.5 * (all_words/all_sentences) - 21.43)
ari = math.ceil(ari)
print(f'ARI of: {ari}')
if ari <= 14:
    age = ari_scale[ari]['ages']
    grade = ari_scale[ari]['grade_level']
    print(f'This is a {grade} level, for people ages {age}.')
else:
    print("Its above your level. ")
