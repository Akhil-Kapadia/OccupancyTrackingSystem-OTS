from django.shortcuts import render

# Create your views here.
import datetime as dt
from .models import Occupancy
from .forms import AddEntry

def home(request):
    currentOccupancy = Occupancy.objects.latest('Time').getOccupancy()
    now = dt.datetime.now()

    return render(request, "home.html", context=
    {
        "currentOccupancy": currentOccupancy,
        "datetime" : now,
        'OccupancyPercentage' : currentOccupancy / 1000
    })
