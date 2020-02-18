from django.db import models

# Create your models here.

class UrlInput(models.Model):
    site_name = models.CharField(max_length=20)
    old_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=20)
    click_count = models.IntegerField()

    def __str__(self):
        return self.site_name + ' ' + self.short_url