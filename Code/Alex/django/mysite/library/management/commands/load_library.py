from django.core.management.base import BaseCommand
import json
import requests
from library.models import Book,Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("/Desktop/class_raccoon/Code/Alex/django/mysite/library/management/commands/books.json", "r") as f:
            books = json.loads(f.read())
        for book in books:
            author = book['author']
            if not Author.objects.filter(author=author).exists():
                author = Author(author=author)
                author.save()
            else:
               author = Author.objects.get(author=author)
            title = book['title']
            year_published = book['year']
            book = Book(title=title, year_published=year_published,author=author)
            book.save()
