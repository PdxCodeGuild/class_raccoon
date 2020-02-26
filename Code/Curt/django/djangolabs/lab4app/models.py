from django.db import models
from django.contrib.auth.models import User
from datetime import date

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

    def checked_out(self):
        return self.checkouts.filter(checked_out=True).exists()

    def checked_by(self):
        checkouts = self.checkouts.filter(checked_out=True)

        if checkouts.exists():
            return checkouts[0].checked_by.username
        return ''

    def checked_date(self):
        checkouts = self.checkouts.filter(checked_out=True)

        if checkouts.exists():
            return checkouts[0].checked_date
        return ''

    def checkin_date(self):
        checkouts = self.checkouts.filter(checkin_date__isnull=False)
        checkouts = checkouts.order_by("-checkin_date")

        if checkouts.exists():
            return checkouts[0].checkin_date
        return ''

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

class Checkout(models.Model):
    checked_out = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='checkouts')
    checked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkouts')
    checked_date = models.DateField(default=date.today)
    checkin_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.checked_out) + ' | ' + str(self.checked_by)