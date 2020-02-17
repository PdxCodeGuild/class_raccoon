from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request,'library/index.html', context)

def view_checked(request):
    pass

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('lab4app:home'))

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('lab4app:home'))
    if next == '':
        return HttpResponseRedirect(reverse('library:login') + '?message=failure')
    return HttpResponseRedirect(reverse('lab4app:login') + '?message=failure&next='+next)

def logout(request):
    pass

def check_in(request):
    pass

def check_out(request):
    pass

