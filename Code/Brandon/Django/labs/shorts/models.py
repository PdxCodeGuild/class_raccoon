from django.db import models

# Create your models here.

class Shorten(models.Model):
    site_name = models.CharField(max_length=50)
    site_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=60)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.site_name