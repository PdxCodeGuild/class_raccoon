from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import random
import string
import math
import re

from .models import ShortUrl
short_chars = string.ascii_lowercase + string.ascii_uppercase +'0123456789-_'

def blankredir(request):
    return redirect(reverse('urlshortener:index'))

def index(request):
    short_list = ShortUrl.objects.order_by('-counter')
    context = {'short_list': short_list}
    return render(request, 'urlshortener/index.html', context)

def saveurl(request):
    if 'long' not in request.POST:
        return redirect('http://tehurn.com/not')
    elif 'short_id' in request.POST:
        long=request.POST['long']
        if re.search(r'https?:\/.*\.\w+', long) == None:
            return HttpResponse("this is a regex non-matching error, this site only accepts http and https pages.")
        short_id = request.POST['short_id']
        edit = ShortUrl.objects.get(id=short_id)
        edit.url = long
        edit.save()
        return redirect(reverse('urlshortener:index'))
    else:
        long=request.POST['long']
        if re.search(r'https:\/.*\.\w+', long) == None:
            return redirect('http://tehurn.com/not')
        code = ''
        shorts_list = ShortUrl.objects.all()
        taken = []
        min = math.log(len(shorts_list))/(6 * math.log(2)) + 2
        if min < 5:
            min = 5
        for shorturl in shorts_list:
            taken.append(shorturl.code)
        while code in taken or len(code) < min:
            code += random.choice(short_chars)
        new = ShortUrl(code=code, url=long, counter=0)
        new.save()
        return redirect(reverse('urlshortener:index'))

def shortened(request, short_code):
    shorty = ShortUrl.objects.get(code=short_code)
    long = shorty.url
    shorty.counter += 1
    shorty.save()
    return redirect(long)
