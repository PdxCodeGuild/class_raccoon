from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import random
import string
from .models import Shorten

# Main index view page
def index(request):
    urls = Shorten.objects.order_by('site_name')
    context = {'urls': urls}
    return render(request,'shorts/index.html',context)

# Creates a new short url but taking the data from th e form on the index page and storing it in the models.
def create(request):
    site_name = request.POST['name']
    site_url = request.POST['url']
    # below will createe the 5 digit/alpha  to bel placed in the url
    lettersAndDigits = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(lettersAndDigits) for i in range(5))

    urls = Shorten(site_name=site_name,site_url=site_url,short_url=short_url, clicks=0)
    urls.save()

    return redirect('shorts:index')

# This takes the data from the model (site url etc) using the short url and redirects to the full site url
def visit(request, short_url):
    urls = Shorten.objects.get(short_url=short_url)
    urls.clicks += 1 
    urls.save()

    return redirect(urls.site_url)

# following function is for removing a url from the database
def delete(request, url_id):
    urls = Shorten.objects.get(id=url_id)
    urls.delete()
    return redirect('shorts:index')

