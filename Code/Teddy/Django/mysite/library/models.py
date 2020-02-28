from django.db import models
from django.contrib.auth.models import User
import datetime

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

class BookCheckout(models.Model):
    checked_out_by = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    checkout_title = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkout')
    checkout_date = models.DateTimeField(auto_now=False)
    checkin_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.checkout_title) + ' Checked out by: ' + str(self.checked_out_by)
