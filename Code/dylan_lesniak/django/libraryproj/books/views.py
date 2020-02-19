from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.utils import timezone
from . import models
import random

# Create your views here.
@login_required
def index(request):
    return render(request, 'books/index.html')

@login_required
def title(request):

    all_books = models.Book.objects.order_by('title')

    # for book in all_books:
    #     if not book.checked_out_by:
    #         available_books.append(book)

    paginator = Paginator(all_books, 10)
    page_number = request.GET.get('page')
    all_books = paginator.get_page(page_number)

    context = {
        'all_books': all_books,
    }
    return render(request, 'books/title.html', context)

@login_required
def author(request):
    all_authors = models.Author.objects.order_by('name')

    paginator = Paginator(all_authors, 10)
    page_number = request.GET.get('page')
    author_obj = paginator.get_page(page_number)

    context = {
        'author_obj': author_obj

    }
    return render(request, 'books/author.html', context)


@login_required
def author_details(request, name):
    author = models.Author.objects.get(name=name)
    
    context = {
        'author': author
    }
    return render(request, 'books/author_details.html', context)
    

@login_required
def book_details(request, book_id):
    book = models.Book.objects.get(id=book_id) #get book from id in url 

    context = {
        'book': book #pass book object to html 
    }
    
    return render(request, 'books/book_details.html', context)

@login_required
def checkout(request, book_id):
    user = request.user
    book = models.Book.objects.get(id=book_id)
    checkout_time = timezone.now()
    new_check = models.BookCheckout(checked_out_by=user, book=book, checkout_date=checkout_time)
    new_check.save()
    return HttpResponseRedirect(reverse('books:title'))

@login_required
def user_details(request):
    user = request.user
    all_books = models.Book.objects.all()
    users_books = []
    for book in all_books:
        if book.checked_out_by() == user:
            users_books.append(book)
    context = {
        'users_books': users_books
    }
    return render(request, 'books/user.html', context)

@login_required
def checkin(request):
    book_id = request.POST['book_id']
    book = models.Book.objects.get(id=book_id)

    book.checkin()

    return HttpResponseRedirect(reverse('books:user_details'))