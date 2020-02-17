from django.core.management.base import BaseCommand
import json
import requests
from library.models import Book,Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("/Users/salamandersmith/Desktop/class_raccoon/Code/Alex/django/mysite/library/management/commands/books.json", "r") as f:
            books = json.loads(f.read())
        for book in books:
            author = book['author']
            if not Author.objects.filter(name=author).exists():
                author = Author(name=author)
                author.save()
            else:
               author = Author.objects.get(name=author)
            #print(f"Author: {author.name}")
            title = book['title']
            #print(f"Title: {title}")
            year_published = book['year']
            #print(f"Year: {year_published}")
            book = Book(title=title, year_published=year_published)
            book.save()
            book.authors.add(author)
            #print("Saving book")

