from django.shortcuts import render
from django.http import HttpResponse
from .models import UrlShorten


# Create your views here.
def index(request):
    urlshort = UrlShorten.objects.all()
    context = {
        'urlshort': urlshort
    }
    return render(request, 'urlshorten/index.html', context)
