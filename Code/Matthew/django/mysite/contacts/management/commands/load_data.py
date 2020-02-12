
from django.core.management.base import BaseCommand
import json
from contacts.models import Contact

class Command(BaseCommand):
    def handle(self, *args, **options):
        Contact.objects.all().delete()
        with open(r'C:\Users\flux\programs\class_raccoon\Code\Matthew\django\mysite\contacts\management\commands\contacts.json', 'r') as f:
            data = f.read()
        data = json.loads(data)
        for data_contact in data['contacts']:
            contact = Contact(**data_contact)
            contact.save()
