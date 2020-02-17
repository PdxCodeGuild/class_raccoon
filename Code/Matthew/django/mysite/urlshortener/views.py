from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import UrlRedirect
import random


@login_required
def index(request):

    # urlredirects = UrlRedirect.objects.all()
    urlredirects = request.user.urlredirects.all()
    # urlredirects = UrlRedirect.objects.filter(user=request.user)
    # urlredirects = UrlRedirect.objects.filter(user_id=request.user.id)
    context = {
        'urlredirects': urlredirects
    }
    return render(request, 'urlshortener/index.html', context)

@login_required
def shorten(request):
    url = request.POST['url']
    code = request.POST['csrfmiddlewaretoken'][:6]
    # code = ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-') for i in range(6)])
    while UrlRedirect.objects.filter(code=code).exists():
        code = ''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-') for i in range(6)])
    counter = 0

    urlredirect = UrlRedirect(code=code, url=url, user=request.user, counter=counter)
    urlredirect.save()

    return HttpResponseRedirect(reverse('urlshortener:index'))



def redirect(request, code):
    urlredirect = UrlRedirect.objects.get(code=code)
    urlredirect.counter += 1
    urlredirect.save()

    return HttpResponseRedirect(urlredirect.url)

@login_required
def detail(request, urlredirect_id):
    urlredirect = UrlRedirect.objects.get(id=urlredirect_id)
    if urlredirect.user.id != request.user.id:
        raise Http404
    context = {
        'urlredirect': urlredirect
    }
    return render(request, 'urlshortener/detail.html', context)

