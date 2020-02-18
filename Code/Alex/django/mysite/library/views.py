from django.shortcuts import render, reverse, redirect
from .models import Author, Book, BooksCheckedOut
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect


def index(request):
    authors = Author.objects.all().order_by('name')
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books,
    }
    return render(request, 'library/index.html', context)



def checked_out(request):

    book = Book.objects.get(id=request.POST['book_id'])
    book.checked_out_by = request.user
    book.save()
    books_checked_out = BooksCheckedOut(checked_out_by=request.user,book=book,checkin_date=None,checkout_date=timezone.now())
    books_checked_out.save()

    return redirect(reverse('library:index'))



def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    records = list(BooksCheckedOut.objects.all().filter(book=book).order_by('-checkout_date'))
    context = {
        'book':book,
        'records':records,
    }

    return render(request, 'library/detail.html', context)



def checked_in(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.checked_out_by:
        book.checked_out_by = None
        book.save()
        books_checked_out = list(BooksCheckedOut.objects.all().filter(book=book))[-1]
        print(books_checked_out)
        books_checked_out.checkin_date = timezone.now()
        books_checked_out.save()

        return redirect(reverse('library:index'))
    return redirect(reverse('library:detail', kwargs={'book_id':book_id}))

