'''
Filename: get_random_text.py
Author: Matthew
Purpose: Gets a random text from a random gutenberg url
'''

import requests
import re
import random

def get_random_book_code():
    response = requests.get('https://www.gutenberg.org/ebooks/search/?sort_order=random')
    text = response.text
    # print(text)
    codes = re.findall('/ebooks/(\d+)', text)
    return random.choice(codes)
    # return random.choice(urls)
    
# https://www.gutenberg.org/files/58714/58714-0.txt
# http://www.gutenberg.org/cache/epub/5785/pg5785.txt
def get_book_text(code):

    url = f'https://www.gutenberg.org/files/{code}/{code}-0.txt'
    response = requests.get(url)
    if response.status_code == 404:
        url = f'http://www.gutenberg.org/cache/epub/{code}/pg{code}.txt'
        response = requests.get(url)

    return response.text

def get_book_title(code):
    response = requests.get('https://www.gutenberg.org/ebooks/' + code)
    text = response.text
    title = re.findall('<h1 itemprop=\"name\">(.+)</h1>', text)
    return title[0]