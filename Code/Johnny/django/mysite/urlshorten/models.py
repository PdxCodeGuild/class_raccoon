from django.db import models

# Create your models here.
class UrlShorten(models.Model):
    user = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    urltoshort = models.CharField(max_length=500)
    counter = models.IntegerField()

    def __str__(self):
        return self.user + ' (' + self.code + ')'
