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
    