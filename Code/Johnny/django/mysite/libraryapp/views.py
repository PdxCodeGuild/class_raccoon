from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

# Create your views here.

def index(request):
    books_data = Book.objects.all()
    available_books = Book.objects.filter(checked_out_by=None)
    print(request.POST)
    print('>>>>')
    print(available_books)
    print('--------')
    context = {
        'books_data' : books_data,
        'available_books': available_books
    }
    return render(request, 'libraryapp/index.html', context)
