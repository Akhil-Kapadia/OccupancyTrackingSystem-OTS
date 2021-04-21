from django.db import models
import datetime
# Create your models here.

class Occupancy(models.Model):
    # Database fields
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Entry = models.BooleanField()
    People = models.PositiveSmallIntegerField(default=1)

    def getOccupancy(self):
        return self.CurrentOccupancy

    class Meta:
        db_table = "Occupancy"
        get_latest_by = 'TimeStamp'

class Doors(models.Model):
    CHOICES = (
        ('OPEN', 'Open Doors'),
        ('CLOSE', 'Close Doors'),
        ('RESET', 'Reset Doors')
    )
    TimeStamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 6, choices = CHOICES)

    class Meta:
        db_table = 'Doors'
        get_latest_by = 'TimeStamp'