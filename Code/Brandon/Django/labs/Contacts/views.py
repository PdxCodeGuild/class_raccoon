from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact



# Create your views here.
def index(request):
    contacts = Contact.objects.order_by('last_name')
    context = {'contacts':contacts}

    return render(request,'Contacts/index.html',context)

def contact_view(request,contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {'contact': contact}

    return render(request,'Contacts/create.html',context)


def new_contact(request):
    first = request.POST['first']
    last = request.POST['last']
    birthday = request.POST['birthday']
    phone = request.POST['phone']

    contact = Contact(first_name=first, last_name=last,birthday=birthday,phone_number=phone)
    contact.save()

    return redirect('Contacts:index')

def edit_contact(request,contact_id):
    contact = Contact.objects.get(id=contact_id)
    first = request.POST['first']
    last = request.POST['last']
    birthday = request.POST['birthday']
    phone = request.POST['phone']

    contact.first_name = first
    contact.last_name = last
    contact.birthday = birthday
    contact.phone_number = phone

    contact.save()
    return redirect('Contacts:index')


def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    print(contact)
    contact.delete()
    return redirect('Contacts:index')

def documentation(request):
    return render(request, 'Contacts/doc.html')

