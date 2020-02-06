from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact



# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}

    return render(request,'Contacts/index.html',context)

def contact_view(request):
    pass

def new_contact(request):
    first = request.POST['first']
    last = request.POST['last']
    birthday = request.POST['birthday']
    phone = request.POST['phone']

    contact = Contact(first_name=first, last_name=last,birthday=birthday,phone_number=phone)
    contact.save()

    return redirect('Contacts:index')

def edit_contact(request):
    pass

