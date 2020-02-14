from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'message' : 'Hello Portland'
    }
    return render(request, 'libraryapp/index.html', context)
