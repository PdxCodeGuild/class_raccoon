from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ContactsList

# Create your views here.
def index(request):
    contact_list = ContactsList.objects.all()
    print(request.POST) # prints dictionary of form submitted
    # print(request.POST['first_name']) # prints dictionary key for first_name
    print(ContactsList.objects.values('id', 'first_name')) # prints out dictionary id and name
    # print(ContactsList.objects.get(id='1')) print out first and last name of first id entry
    context = {
    'contact_list': contact_list
    }
    return render(request, 'contactsapp/index.html', context)

def create(request):
    print(request.POST)
    create_first_name = request.POST['first_name']
    create_last_name = request.POST['last_name']
    create_birthday = request.POST['birthday']
    create_phone_number = request.POST['phone_number']
    create_is_cell = request.POST['is_cell']
    # checks to see if is_cell is in dictionary of request.POST from forms.
    # if is_cell in request.POST if/else statements

    if request.POST['is_cell'] == 'on':
        create_is_cell = True
    else:
        create_is_cell = False
    contact = ContactsList(first_name=create_first_name,
                            last_name=create_last_name,
                            birthday=create_birthday,
                            phone_number=create_phone_number,
                            is_cell=create_is_cell)
    contact.save()
    return HttpResponseRedirect(reverse('contactsapp:index'))


def delete(request, contact_id):
    contact = ContactsList.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contactsapp:index'))


def edit(request, contact_id):
    contact = ContactsList.objects.get(id=contact_id)
    edit_contact = {
        'contact': contact
    }
    return render(request, 'contactsapp/edit.html', edit_contact)
