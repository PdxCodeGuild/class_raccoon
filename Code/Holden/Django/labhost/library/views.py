from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Book, Author, BookCheckout, Checkout
import datetime

def index(request):
    books = Book.objects.all()
    context = {
    'books': books
    }
    return render(request, 'library/index.html', context)

def book_view(request, book_id):
    message = request.GET.get('message', '')
    book = Book.objects.get(id=book_id)
    copies = BookCheckout.objects.filter(book=book)
    copies_checked = 0
    all_copies = 0
    for copy in copies:
        available = None
        if copy.checkout_date == None:
            if available == None:
                available = True
        else:
            copies_checked += 1
        all_copies += 1

    context = {
    'book': book, 'unchecked': available, 'checked': copies_checked, 'copies': all_copies, 'message': message,
    }
    return render(request, 'library/book_view.html', context)

@login_required
def book_checkout(request, book_id):
    copies = BookCheckout.objects.filter(book__id=book_id)
    for copy_iter in copies:
        if copy_iter.checkout_date == None:
            copy = copy_iter
            break
    else:
        return redirect(reverse('library:book_view', args=(copy.book.id,)) + '?message=checkout_error')
    user = request.user
    copy.checked_out_by = user
    copy.checkout_date = datetime.datetime.now()
    copy.save()
    return redirect(reverse('library:index'))

@login_required
def checkin(request, checkout_id):
    user = request.user
    copy = BookCheckout.objects.get(id=checkout_id)
    if user != copy.checked_out_by:
        return HttpResponseNotFound()
    prevcheckin = copy.checkin_date
    prevcheckout = copy.checkout_date
    new = Checkout(book_copy=copy, checkin_date=prevcheckin, checkout_date=prevcheckout, username=user.username)
    copy.checkout_date = None
    copy.checkin_date = datetime.datetime.now()
    copy.checked_out_by = None
    new.save()
    copy.save()
    return redirect(reverse('library:user_checkouts'))

@login_required
def user_checkouts(request):
    user = request.user
    user_books = user.checkouts.order_by('checkout_date')
    context = {
    'books': user_books
    }
    return render(request, 'library/user_checkouts.html', context)