from django.db import models

class Contact(models.Model):
    # id = models.IntegerField...
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateTimeField('Birth date')
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name +' '+ self.last_name 
