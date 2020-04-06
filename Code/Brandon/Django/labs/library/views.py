from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Book, Author, BookCheckout

# Create your views here.
def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request,'library/index.html', context)

@login_required
def view(request):
##   request.user.book_checkouts.all()
    books = BookCheckout.objects.all().filter(checked_out_by = request.user)

    book_views = Book.objects.order_by('author')
    if request.method == 'POST':
        search_text = request.POST['search_text']
        book_views = book_views.filter(title__icontains=search_text)
    context={
        'books':books,
        'book_views':book_views
    }

    return render(request,'library/view.html',context)


def register(request):
    if request.method == 'GET':
        return render(request, 'library/register.html')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
#    login(request, user)

    return HttpResponseRedirect(reverse('library:login'))

def login_user(request):
    if request.method == 'GET':
        return render(request, 'library/login.html')

    username = request.POST['username']
    password = request.POST['password']
    next = request.GET.get('next','')
    print(request.POST)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('library:index'))
    if next == '':
        return HttpResponseRedirect(reverse('library:login') + '?message=failure')
    return HttpResponseRedirect(reverse('library:index') + '?message=failure&next='+next)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('library:index') + '?message=loggedout')

def check_in(request):
    pass

#@login_required
def check_out(request, book_id):
    book = Book.objects.get(id=book_id)
    # create a new checkout model using this book
    checkout = BookCheckout(checked_out_by=request.user, book=book, checkout_date=timezone.now(), checkin_date=None)
    # and the logged in user (request.user)
    checkout.save()

    return HttpResponseRedirect(reverse('library:view'))














