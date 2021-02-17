from django.shortcuts import render

# Create your views here.
import datetime as dt
from .models import Occupancy
from .forms import AddEntry

def home(request):
    currentOccupancy = Occupancy.objects.latest('Time').getOccupancy()
    now = dt.datetime.now()
    #Forms
    manualAdd = AddEntry(request.POST or None, request.FILES or None)
    
    if manualAdd.is_valid():
        manualAdd.save()

    return render(request, "home.html", context=
    {
        "currentOccupancy": currentOccupancy,
        "datetime" : now,
        'manualAdd' : manualAdd,
        'OccupancyPercentage' : currentOccupancy/10000
    })
