from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Author, Books, Book_checkout
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    
    authors = Author.objects.all()
    books = Books.objects.all()
    checkout = Book_checkout.objects.all()

    context = {
        'authors':authors,
        'books':books,
        'checkout':checkout, 
    }
    return render(request, 'library/index.html', context)

@login_required
def checkout(request, bookid):
    print("You checked out a book, good job nerd")

    book = Books.objects.get(id=bookid)
    book.checked_out = True
    book.checked_out_by = request.user
    book.save()
    record = Book_checkout(book = book, checked_out_by = request.user, checkout_date = timezone.now())
    record.save()

    return redirect(reverse('library:index'))

@login_required
def checkin(request, bookid):
    print('Klaatu barada nikto')

    book = Books.objects.get(id=bookid)
    book.checked_out = False
    book.checked_out_by = None
    book.save()
    record = list(book.records.all())[-1]
    record.checkin_date = timezone.now()
    record.save()

    return redirect(reverse('library:mybooks'))
    
    

@login_required
def mybooks(request):
    print("These are your books, nerd")
    books = Books.objects.all().filter(checked_out_by=request.user)

    context={
        'books':books
    }

    return render(request, 'library/details.html', context)