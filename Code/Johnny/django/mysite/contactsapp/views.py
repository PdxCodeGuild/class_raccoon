from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ContactsList

# Create your views here.
def index(request):
    contact_list = ContactsList.objects.all()
    context = {
    'contact_list': contact_list
    }
    return render(request, 'contactsapp/index.html', context)
