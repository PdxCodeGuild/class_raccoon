from django.db import models


class Shortener(models.Model):
    code = models.CharField(max_length=6)
    url = models.CharField(max_length=2048)

    def __str__(self):
        return self.code
