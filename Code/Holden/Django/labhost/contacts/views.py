from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime

from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.order_by('last_name')
    context = {'contacts': contacts}
    return render(request, 'contacts/index.html', context)

def contact_detail(request, contact):
    contact_data = Contact.objects.get(id=contact)
    birthday = contact_data.birthday
    context = {'contact_data': contact_data, 'birthday': birthday}
    return render(request, 'contacts/detail.html', context)

def new_contact(request):
    return render(request, 'contacts/new.html')

def edit_contact(request, contact):
    contact_data = Contact.objects.get(id=contact)
    context = {'contact_data': contact_data}
    return render(request, 'contacts/index.html', context)

def write_new_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    if last_name == '':
        return HttpResponseRedirect(reverse(index))
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    if 'is_cell' in request.POST:
        is_cell = True
    else:
        is_cell = False
    print(birthday)
    new = Contact(first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, is_cell=is_cell)
    new.save()
    return HttpResponseRedirect(reverse('contacts:index'))

def write_edit_contact(request, contact):
    contact_data = Contact.objects.get(id=contact)
    return HttpResponse('you are at the edit page for '+str(contact))
