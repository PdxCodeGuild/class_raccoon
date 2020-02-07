from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
import datetime
#HttpResponse(reverse("lab2app:index"))

def index(request):
    return HttpResponse("This is the index page.")

def contacts(request):
    contact_list = Contact.objects.all()
    context = {
        "contact_list": contact_list
    }
    return render(request, "lab2app/contacts.html", context)

def contact_id(request, contact_item_id):
    contact_details = Contact.objects.get(id=contact_item_id)
    context = {
        "contact_details": contact_details
    }
    return render(request, "lab2app/contact_id.html", context)

def new_contact(request):
    return HttpResponse("This is the new contacts page")

def edit_contact(request, contact_item_id):
    contact_details = Contact.objects.get(id=contact_item_id)
    context = {
        "contact_details": contact_details
    }
    return render(request, "lab2app/edit_contact.html", context)

def new_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    if 'is_cell' in request.POST:
        is_cell = True
        cellstat = "Yes"
    else:
        is_cell = False
        cellstat = "No"

    birthday = birthday.replace('/','-')
    print(request.POST)
    new_contact = Contact(first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, is_cell=is_cell)

    # save the instance
    new_contact.save()

    # redirect back to the index view
    return HttpResponseRedirect(reverse('lab2app:contacts'))

def update_contact(request, contact_item_id):
    contact_details = Contact.objects.get(id=contact_item_id)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    if 'is_cell' in request.POST:
        is_cell = True
        cellstat = "Yes"
    else:
        is_cell = False
        cellstat = "No"

    birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d').date()
    # birthday = date(birthday).isoformat()

    contact_details.first_name = first_name
    contact_details.last_name = last_name
    contact_details.birthday = birthday
    contact_details.phone_number = phone_number
    contact_details.is_cell = is_cell
    contact_details.cellstat = cellstat

    # save the instance
    contact_details.save()

    # redirect back to the index view
    return HttpResponseRedirect(reverse('lab2app:contacts'))

def delete_contact(request, contact_item_id):
    Contact.objects.filter(id=contact_item_id).delete()
    return HttpResponseRedirect(reverse('lab2app:contacts'))
