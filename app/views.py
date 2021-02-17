from django.shortcuts import render

# Create your views here.
import datetime
from .models import Occupancy

def home(request):
    currentOccupancy = Occupancy.CurrentOccupancy
    now = datetime.datetime.now()
    return render(request, "home.html",context=
    {
        "currentOccupancy": currentOccupancy,
        "datetime" : now
    })
