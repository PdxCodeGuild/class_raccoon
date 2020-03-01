from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book, Author, BookCheckout
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()

    context = {
        'books': books,
        'authors': authors,
        }
    return render(request, 'library/index.html', context)

def checkout(request):
    checkout = Book.objects.all()
    book_number = request.POST['checkout']
    book_tocheckout = Book.objects.get(id=book_number)
    user_checkout = User.objects.get(id=1)

    checkingout = BookCheckout(checked_out_by=user_checkout, checkout_title=book_tocheckout, checkout_date=datetime.now())
    checkingout.save()

    checkout1 = Book.objects.filter(id=book_number).update(checked_out_by=user_checkout)
    return HttpResponseRedirect(reverse('library:index'))
