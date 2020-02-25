from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        authors = self.authors.all()
        return self.title + ", " + authors[0].name

    def authorlist(self):
        authors = self.authors.all()
        if len(authors) != 0:
            authlist = ', '.join(author.name for author in authors)
        else:
            authlist = 'author error'
        return authlist

class BookCheckout(models.Model):
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='checkouts')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='copies')
    checkout_date = models.DateTimeField(null=True, blank=True)
    checkin_date = models.DateTimeField()

    def __str__(self):
        checked = ''
        if self.checkout_date:
            checked = ' - checked out'
        return self.book.title + ' id ' + str(self.id) + checked

class Checkout(models.Model):
    book_copy = models.ForeignKey(BookCheckout, on_delete=models.CASCADE, related_name='checkout_history')
    username = models.CharField(max_length=150)
    checkout_date = models.DateTimeField()
    checkin_date = models.DateTimeField()

    def __str__(self):
        return self.book_copy.book.title + ', ' + self.checkin_date.strftime('%m-%d-%Y, %I:%M:%S%p') + ' - ' + self.username

    class Meta:
        ordering = ['checkin_date']