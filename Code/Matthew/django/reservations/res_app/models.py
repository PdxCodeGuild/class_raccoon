from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    tables = models.IntegerField()

    def __str__(self):
        return self.name + " Tables: " + str(self.tables)

class Reservation(models.Model):
    party_name = models.CharField(max_length=50)
    time = models.DateTimeField()
    party_size = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name="reservations")

    def __str__(self):
        return self.restaurant.name + ": " + self.party_name