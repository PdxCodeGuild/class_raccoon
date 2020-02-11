from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact

def index(request):
    contacts = Contact.objects.all()

    context = {
        'title': 'Contacts List ',
        'error': '',
        'contacts': contacts,
    }
    return render(request, 'contactsapp/index.html', context)

def savecontact(request):
    print(request.POST)

    # get data out of dictionary
    firstname_text = request.POST['firstname_text']
    lastname_text = request.POST['lastname_text']
    birthdate_text = request.POST['birthdate_text']
    phone_text = request.POST['phone_text']

    contact = Contact(first_name = firstname_text, last_name=lastname_text, birthday=birthdate_text, phone_number=phone_text)

    # save the instance
    contact.save()

    # redirect back to the index view
    return HttpResponseRedirect(reverse('contactsapp:index'))

def deletecontact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contactsapp:index'))
