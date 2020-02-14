from django.db import models
from django.contrib.auth.models import User

class Url_short(models.Model):
    source_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=20)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return str(self.counter) + ' | ' + self.source_url + ' | ' + self.short_url