from django.db import models
import datetime

class Contact(models.Model):
    # id = models.IntegerField...
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birthday = models.DateField('Birth date')
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name +' '+ self.last_name
