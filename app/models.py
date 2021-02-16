from django.db import models
import datetime
# Create your models here.

class Occupancy(models.Model):
    # Database fields
    Date = models.DateField(auto_now_add=True)
    Time = models.DateTimeField(auto_now=True)
    Entry = models.BooleanField()
    People = models.PositiveSmallIntegerField(default=1)
    CurrentOccupany = models.PositiveSmallIntegerField(null=True)