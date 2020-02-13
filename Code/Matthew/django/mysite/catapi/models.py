from django.db import models

class CatImage(models.Model):
    cat_api_id = models.CharField(max_length=20)
    url = models.CharField(max_length=500)
    favorite = models.BooleanField()

    def __str__(self):
        return self.cat_api_id + ' ' + self.url




