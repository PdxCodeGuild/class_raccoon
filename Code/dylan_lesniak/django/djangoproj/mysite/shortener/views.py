from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Short
import string

def index(request):
    urls = Short.objects.all()
    context = {
        'urls': urls
    }

    return render(request, 'shortener/index.html', context)


#form sends info to generate url function
#url function creates a shortened url checked against a list of all shortened urls 
#creates another one until it's no longer matched. Theoretically possible for an infinite loop
#don't forget to create a base.html for headers 

def new_url(request):
    print(request.POST)
    longform = request.POST['longform']
    shortform = shorten(longform)
    url = Short(shortform=shortform, longform=longform)
    url.save()

    return HttpResponseRedirect(reverse('shortener:index'))

def redirect(request, shortform):
    print(request.POST)
    url_object = Short.objects.get(shortform=shortform)
    longform = url_object.longform
    return HttpResponseRedirect(longform)


    

#helper methods
def shorten(longform):
    num_of_records = Short.objects.count()
    print(num_of_records)
    letters = string.ascii_letters
    shortened_url = ""
    # while possible_combinations < num_of_records: #might not need this...
    #     num_of_chars *= 2
    
    previous_url = Short.objects.all().last().shortform
    prev_last_letter = previous_url[-1]
    if previous_url == letters[-1]:
        shortened_url = previous_url + letters[0]
    else:
        letters_idx = letters.find(prev_last_letter)
        letters_idx += 1
        previous_url = list(previous_url)
        previous_url = previous_url[:-1]
        new_letter = letters[letters_idx]
        previous_url = "".join(previous_url)
        shortened_url = previous_url + new_letter
    return shortened_url
    
