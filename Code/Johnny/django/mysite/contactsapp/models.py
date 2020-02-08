from django.db import models

# Create your models here.
class ContactsList(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    is_cell = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
