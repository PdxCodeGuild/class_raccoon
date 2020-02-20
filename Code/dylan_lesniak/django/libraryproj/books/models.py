from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
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
    # checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def checked_out_by(self):
        checkouts = self.checkouts.filter(checkin_date__isnull=True) #gives us any checkouts that haven't been turned in yet. 
        if checkouts.exists():
            return checkouts[0].checked_out_by
        return None 

    def checkout_date(self):
        checkouts = self.checkouts.filter(checkin_date__isnull=True)
        if checkouts.exists():
            return checkouts[0].checkout_date
        return None

    def checkin(self):
        checkouts = self.checkouts.filter(checkin_date__isnull=True)
        checkout = checkouts[0]
        checkout.checkin_date = timezone.now()
        checkout.save()
        


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class BookCheckout(models.Model):
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="checkouts")
    checkout_date = models.DateTimeField()
    checkin_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['book']

    def __str__(self):
        return f"'{self.book}' was checked out by {self.checked_out_by} on {self.checkout_date}."

