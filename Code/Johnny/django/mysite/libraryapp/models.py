from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author')
    checked_out_by = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title + ' (' + str(self.author) + ')'
