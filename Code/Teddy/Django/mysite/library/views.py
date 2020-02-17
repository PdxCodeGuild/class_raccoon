from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book, Author

def index(request):

    authors = Author.objects.all()
    books = Book.objects.all()

    context = {
        'books': books,
        'authors': authors,
        }
    return render(request, 'library/index.html', context)
