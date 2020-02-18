from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    author=models.CharField(max_length=30)

    def __str__(self):
        return self.author


class Books(models.Model):
    title=models.CharField(max_length=50)
    publish_date=models.DateTimeField()
    author=models.ForeignKey(Author, on_delete=models.PROTECT)
    checked_out=models.BooleanField()
    checked_out_by=models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.title

    


class Book_checkout(models.Model):
    checked_out_by=models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    book=models.ForeignKey(Books, on_delete=models.PROTECT, related_name= 'records')
    checkout_date=models.DateField()
    checkin_date=models.DateField(blank=True, null=True) 

    def __str__(self):
        return self.checked_out_by.username
    


