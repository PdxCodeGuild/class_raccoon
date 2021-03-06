from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date
import requests

from . import secrets
from .models import Author, Book, Checkout

@login_required()
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors,
    }
    return render(request, 'lab4app/index.html', context)

@login_required()
def togglecheckout(request, book_id):
    book = Book.objects.get(id=book_id)
    checkouts = book.checkouts.filter(checked_out=True)
    if checkouts.exists(): # check back in
        checkout = checkouts[0]
        if checkout.checked_by == request.user:
            checkout.checked_out = False
            checkout.checkin_date = date.today()
            checkout.save()
    else: # check out
        # create a new checkout, and save it
        checked_date = date.today()
        checkout = Checkout(checked_out = True, book = book, checked_by = request.user, checked_date = checked_date)
        checkout.save()

    return HttpResponseRedirect(reverse('lab4app:index'))

@login_required()
def bookview(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    context = {
        'book':book,
        'authors':authors,
    }
    return render(request, 'lab4app/book.html', context)

def register(request):
    return render(request, 'lab4app/register.html')

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('lab4app:home'))


def login_page(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    context = {
        'next': next,
        'message': message
    }
    return render(request, 'lab4app/login.html', context)


def login_user(request):

    next = request.POST['next']
    recaptcha_response = request.POST.get('g-recaptcha-response')
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {
        'secret': secrets.google_recaptcha_key,
        'response': recaptcha_response
    })
    result = r.json()
    if not result['success']:
        return HttpResponseRedirect(reverse('lab4app:login') + '?message=invalid_recaptcha&next='+next)



    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('lab4app:home'))
    if next == '':
        return HttpResponseRedirect(reverse('lab4app:login') + '?message=failure')
    return HttpResponseRedirect(reverse('lab4app:login') + '?message=failure&next='+next)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('lab4app:login') + '?message=loggedout')

@login_required()
def home(request):
    return render(request, 'lab4app/home.html')

@login_required()
def profile(request):
    return render(request, 'lab4app/profile.html')