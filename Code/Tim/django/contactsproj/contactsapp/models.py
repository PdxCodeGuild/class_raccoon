from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.birthday, self.phone)
