from django.core.management.base import BaseCommand
import json

from library.models import Book,Author, BookCheckout


class Command(BaseCommand):
    def handle(self, *args, **options):
        BookCheckout.objects.all().delete()

        Book.objects.all().delete()
        with open(r"C:\Users\Brandon\code\class_raccoon\Code\Brandon\Django\labs\library\management\commands\books.json", "r") as f:
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
            url = book['link']
            book = Book(title=title, year_published=year_published,author=author, url=url)
            book.save()
            


