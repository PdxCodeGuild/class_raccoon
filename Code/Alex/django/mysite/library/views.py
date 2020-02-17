from django.shortcuts import render
from .models import Author, Book


def index(request):
    authors = Author.objects.all().order_by('name')
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books,
    }
    return render(request, 'library/index.html', context)

def checked_out_or_not(request):
    context = {
        'checked_out_by':checked_out_by,
    }
    return render(request, 'library/index.html', context)