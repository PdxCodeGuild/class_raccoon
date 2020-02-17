from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return '\"' + self.title + '\"' + ' by ' + ', '.join([author.name for author in self.authors.all()])


class BooksCheckedOut(models.Model):
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '\"' + self.book.title + '\"' + ' by ' + ', '.join([author.name for author in self.book.authors.all()])