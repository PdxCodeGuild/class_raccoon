from django.db import models

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

class User(models.Model):
    pass

    

    
