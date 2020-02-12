from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def index(request):
    return HttpResponse('one view that returns a page for entering in a url to be shortened, and possibly a list of entries')



def saveurl(request):
    return HttpResponse('another view and view for receiving the POSTed url, generating a random string, and saving it to the database')



def redirect(request):
    return HttpResponse('a third view that performs the redirecting (localhost/redirect/pEc4vt), you could use redirect or HttpResponseRedirect. Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.')