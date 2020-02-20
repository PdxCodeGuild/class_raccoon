from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import UrlInput

# Create your views here.

def index(request):
    urls = UrlInput.objects.all()

    context = {
    'urls' : urls
    }
    return render(request, 'urlshort/index.html', context)

def saveurl(request):
    print(request.POST)
    site_name = request.POST['site_name']
    old_url = request.POST['old_url']
    short_url = request.POST['csrfmiddlewaretoken'][:5]
    
    url = UrlInput(site_name=site_name, old_url=old_url, short_url=short_url, click_count=0)
    url.save()

    return redirect(reverse('urlshort:index'))

def sendit(request, stub):
    try:
        url = UrlInput.objects.get(short_url=stub)
        url.click_count +=1
        url.save()
    except:
        return redirect(reverse('urlshort:index'))

    return redirect(url.old_url)