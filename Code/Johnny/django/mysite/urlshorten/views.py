from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlShorten
import string
import random
import webbrowser


# Create your views here.
def index(request):
    urlshort = UrlShorten.objects.all()
    context = {
        'urlshort': urlshort
    }
    return render(request, 'urlshorten/index.html', context)

def createurl(request):
    print(request.POST)
    user = request.POST['user']
    urltoshort = request.POST['urltoshort']
    code = []
    L = 5
    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k = L))
    print(code1)
    new_user = UrlShorten(user=user,
                            code=code1,
                            urltoshort=urltoshort,
                            counter=0)
    new_user.save()
    return HttpResponseRedirect(reverse('urlshorten:index'))

def visit(request, code): # code param comes from URLS.PY
    data = UrlShorten.objects.get(id=code)
    print(data.urltoshort)
    data.counter = data.counter +1
    data.save()
    webbrowser.open_new(f'{data.urltoshort}')
    print(data)
    print(data.counter)
    return HttpResponseRedirect(reverse('urlshorten:index'))
