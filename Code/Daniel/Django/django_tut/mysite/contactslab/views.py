from django.shortcuts import render
from .models import ContactInfo


# Create your views here.

def index(request):

    contacts = ContactInfo.objects.all()
    
    
    context = {
        'contacts' : contacts
    }
    return render(request, 'contactslab/index.html', context)