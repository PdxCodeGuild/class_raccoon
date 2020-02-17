from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request,'library/index.html', context) 

