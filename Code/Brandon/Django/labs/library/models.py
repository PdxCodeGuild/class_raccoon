from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Book(models.Model):
    title = models.CharField(max_length=100)
    year_published = models.CharField(max_length=4)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.author.author + ' ' + self.title

class BookCheckout(models.Model):
    checked_out_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='book_checkouts')
    book = models.ForeignKey(Book, on_delete=models.PROTECT,)
    checkout_date = models.DateTimeField()
    checkin_date = models.DateTimeField(null=True, blank=True, default=None)

#    def __str__(self):
#        return self.


    

    
