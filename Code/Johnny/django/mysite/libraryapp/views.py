from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author, BookCheckout
from django.contrib.auth.models import User
from datetime import datetime

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
    book_tocheckout = Book.objects.get(id=book_number) #returns post info of what book\
    user_checkout = User.objects.get(id=1)
    print(user_checkout)
    # saving info to BookCheckout database
    checkingout = BookCheckout(checkout_checked_out_by=user_checkout,
                                checkout_title=book_tocheckout,
                                checkout_date=datetime.now())
    checkingout.save()
    # MyModel.objects.filter(pk=some_value).update(field1='some value')
    # updating the Model field with checkout and return to index view
    checkout1 = Book.objects.filter(id=book_number).update(checked_out_by=user_checkout)
    return HttpResponseRedirect(reverse('libraryapp:index'))

def checkin(request, checkin):
    book_info = Book.objects.all()
    get_book = Book.objects.filter(id=checkin)
    book_details = BookCheckout.objects.filter(checkout_title_id=checkin)
    context = {
        'book_info': book_info,
        'get_book': get_book,
        'book_details': book_details,
    }
    return render(request, 'libraryapp/checkin.html', context)
