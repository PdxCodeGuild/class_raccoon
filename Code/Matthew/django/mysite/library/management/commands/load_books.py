



from django.core.management.base import BaseCommand
from library.models import Book, Author
import json
import requests
import random






class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./library/management/commands/words.txt','r') as file:
            words = file.read()
        words = words.split('\n')
        for i in range(40):
            random_word = random.choice(words)
            print(f"Searching for book: {random_word}.")
            response = requests.get('http://openlibrary.org/search.json?q=' + random_word)
            data = json.loads(response.text)
            if len(data['docs']) == 0:
                continue
            book_data = random.choice(data['docs'])
            title = book_data['title']
            if 'first_publish_year' not in book_data:
                continue
            year_published = book_data['first_publish_year']

            authors = book_data.get('author_name',['No Author']) #get or create for this.

            if Book.objects.filter(title=title, year_published=year_published).exists():
                continue

            book = Book(title=title, year_published=year_published)
            book.save()

            for author in authors:
                author, created = Author.objects.get_or_create(name=author)
                book.authors.add(author)

            print(str(round(i/40*100, 2))+'%')




'''
STEPS to Populate Database:
- Load words from words.txt
- Get random word from that selection
- Apply that to query string (?key=str)
- Get data from query (Json to python dict)
- Grab random book from this selection
- Load said random data into database

'''

'''
EDGE CASES:
if len(list)==0, try again
Try except

'''