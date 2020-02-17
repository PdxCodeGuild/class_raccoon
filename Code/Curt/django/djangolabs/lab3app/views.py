from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import string, random

from .models import Url_short

#HttpResponse(reverse("lab2app:index"))

def index(request):
    url_list = Url_short.objects.order_by('-id')
    context = {
        'url_list': url_list
    }
    return render(request, 'lab3app/index.html', context)

def shorten(request):
    source_url = request.POST['url']
    charstr = string.ascii_letters + string.digits

    short_url = ''.join([random.choice(charstr) for i in range(6)])
    while Url_short.objects.filter(short_url=short_url).exists():
        short_url = ''.join([random.choice(charstr) for i in range(6)])
    counter = 0

    url_list = Url_short(source_url=source_url, short_url=short_url, counter=counter)
    url_list.save()

    return HttpResponseRedirect(reverse('lab3app:index'))

# def redirect(request, code):
#     urlredirect = UrlRedirect.objects.get(code=code)