from django.shortcuts import render, redirect, reverse
from .models import ContactInfo, PhoneType


# Create your views here.

def index(request):
    contacts = ContactInfo.objects.all()
    phone_types = PhoneType.objects.all()
    context = {
        'contacts' : contacts,
        'phone_types' : phone_types,
    }
    return render(request, 'contactslab/index.html', context)

def create(request):
    print(request.POST)
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    birthday = request.POST['brthday']
    phone_number = request.POST['phnumber']
    phone_type = request.POST['phonetype']
    phone_type = PhoneType.objects.get(id=phone_type)
    contact = ContactInfo(
        first_name = first_name,
        last_name = last_name,
        birthday = birthday,
        phone_number = phone_number,
        phone_type = phone_type

    )
    contact.save()
    
    return redirect(reverse('contactslab:index'))

def update(request):
    contact = ContactInfo.objects.get(id=request.POST['contactid'])
    contact.first_name = request.POST['firstname']
    contact.last_name = request.POST['lastname']
    contact.birthday = request.POST['brthday']
    contact.phone_number = request.POST['phnumber']
    phone_type = request.POST['phonetype']
    phone_type = PhoneType.objects.get(id=phone_type)
    contact.phone_type = phone_type
    contact.save()
    
    return redirect(reverse('contactslab:index'))

def delete(request, contactid):
    contact = ContactInfo.objects.get(id=contactid)
    contact.delete()

    return redirect(reverse('contactslab:index'))


    