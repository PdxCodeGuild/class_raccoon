from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField('birthday', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_cell = models.BooleanField(blank=True)
    def __str__(self):
        output = ""
        if self.first_name:
            output += self.first_name + ' '
        output += self.last_name
        return output
