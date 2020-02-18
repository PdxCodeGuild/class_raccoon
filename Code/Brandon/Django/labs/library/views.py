from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
    context={
        'books':books
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

def check_out(request):
    pass






