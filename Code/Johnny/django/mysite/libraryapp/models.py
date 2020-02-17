from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author')
    checked_out_by = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title + ' (' + str(self.author) + ')'

class BookCheckout(models.Model):
    checkout_checked_out_by = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    checkout_title = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkout')
    checkout_date = models.DateTimeField(auto_now=False)
    checkin_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.checkout_title) + ' Out: ' + str(self.checkout_checked_out_by)
