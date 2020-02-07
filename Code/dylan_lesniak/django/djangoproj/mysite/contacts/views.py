from django.shortcuts import reverse, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
import datetime

# Create your views here.
def index(request): 
    contacts = Contact.objects.order_by('last_name')
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


def details(request, contact_id):
    # get the contact with the given id
    # pass the contact to the template to be rendered
    person = Contact.objects.get(id=contact_id)
    person.phone_number = format_phone(person.phone_number)
    context = {
        'person': person
    }
    return render(request, 'contacts/details.html', context)

def edit(request, contact_id):
    person = Contact.objects.get(id=contact_id)
    person.phone_number = format_phone(person.phone_number)
    context = {
        'person': person
    }
    return render(request, 'contacts/edit.html', context)

def save_edit(request, contact_id):
    person = Contact.objects.get(id=contact_id)
    person.first_name = request.POST['first_name']
    person.last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    person.birthday = birthday
    person.phone_number = request.POST['phone_number']
    person.save()
    return HttpResponseRedirect(reverse('contacts:details', args=(contact_id,)))

def new_form(request):
    return render(request, 'contacts/new_form.html')

def save_new_form(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    phone_number = request.POST['phone_number']
    person = Contact(first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number)
    person.save()
    return HttpResponseRedirect(reverse('contacts:index'))

def delete(request, contact_id):
    person = Contact.objects.get(id=contact_id)
    person.delete()

    return HttpResponseRedirect(reverse('contacts:index'))

def format_phone(number_str):
    temp_num = ""
    for char in number_str:
        if char.isdigit():
            temp_num += char 

    number_str = temp_num
    temp_num = ""
    count = 0 
    while len(number_str) < 10:
        number_str = "x" + number_str

    for i in range(10):
        if i == 0:
            temp_num += "(" + number_str[i]
        elif i == 3:
            temp_num += ")" + number_str[i]
        elif i == 6:
            temp_num += "-" + number_str[i]
        else:
            temp_num += number_str[i]
    return temp_num
