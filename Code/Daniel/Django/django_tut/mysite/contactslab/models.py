from django.db import models

# Create your models here.

class PhoneType(models.Model):
    phone_type = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_type

class ContactInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + self.last_name