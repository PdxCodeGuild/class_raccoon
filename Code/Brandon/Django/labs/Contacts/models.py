from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12)
    is_cell = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

