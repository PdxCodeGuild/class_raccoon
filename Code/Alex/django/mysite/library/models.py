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
    pages = models.IntegerField()
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    link = models.TextField()

    # def checked_out_by(self):
    #     checkout = self.bookscheckedout_set.filter(checkin_date__isnull=True)
    #     if checkout.exists():
    #         return checkout[0].checked_out_by
    #     return None


    def __str__(self):
        return '\"' + self.title + '\"' + ' by ' + ', '.join([author.name for author in self.authors.all()])


class BooksCheckedOut(models.Model):
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '\"' + self.book.title + '\"' + ' by ' + ', '.join([author.name for author in self.book.authors.all()])