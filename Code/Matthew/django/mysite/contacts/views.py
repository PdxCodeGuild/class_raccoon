from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import re

from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    return render(request, 'contacts/detail.html', {})


# <QueryDict: {'csrfmiddlewaretoken': ['OLsfFgImyzNtypFlHDDBIvgsjsIZY9n5PDdwGp3rwPu7QQytrr8MEO7P0vRvMBcl'], 'contact_first_name': ['A'], 'contact_last_name': ['B'], 'contact_birthday': ['2021-03-12'], 'contact_phone_number': ['C'], 'contact_comments': ['D']}>
def savecontact(request):
    # print(request.POST)

    contact_id = request.POST.get('contact_id', '')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    comments = request.POST['comments']

    if first_name == '' or last_name == '' or birthday == '' or phone_number == '' or comments == '':
        return HttpResponseRedirect(reverse('contacts:index'))


    match = re.match(r'^\(?(\d{3})[)\- ]*(\d{3})[\- ]?(\d{4})$', phone_number)
    phone_number = match.group(1) + match.group(2) + match.group(3)

    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date() # this line is optional :O

    if contact_id == '':
        new_contact = Contact(first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, comments=comments)
        new_contact.save()
    else:
        contact = Contact.objects.get(id=contact_id)
        contact.first_name = first_name
        contact.last_name = last_name
        contact.birthday = birthday
        contact.phone_number = phone_number
        contact.comments = comments
        contact.save()

    return HttpResponseRedirect(reverse('contacts:index'))



def edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/edit.html', context)


def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts:index'))

