from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author, BookCheckout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    books_data = Book.objects.all()
    available_books = Book.objects.filter(checked_out_by=None)
    # print(request.POST)
    # print('>>>>')
    # print(available_books)
    # print('--------')
    context = {
        'books_data' : books_data,
        'available_books': available_books
    }
    return render(request, 'libraryapp/index.html', context)

# getting info to post to user field

def checkout(request):
    print('POSTING CHECKOUT INFO')
    print(request.POST)
    checkout = Book.objects.all() #returns the model of BOOK
    book_number = request.POST['checkout']
    book_tocheckout = Book.objects.get(id=book_number) #returns post info of what book

    return HttpResponseRedirect(reverse('libraryapp:index'))
