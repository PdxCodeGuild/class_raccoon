from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request,'library/index.html', context)

def view_checked(request):
    pass

def register(request):
    pass

def login(request):
    pass

def logout(request):
    pass

def check_in(request):
    pass

def check_out(request):
    pass

