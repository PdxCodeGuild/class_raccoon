from django.db import models

# Create your models here.
class RPSGame(models.Model):
    playerchoice = models.CharField(max_length=10)
    compchoice = models.CharField(max_length=10)
    playername = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    humanwin = models.BooleanField()

    def __str__ (self):
        return self.playername + " " + str(self.timestamp) + " Win:" + str(self.humanwin)

