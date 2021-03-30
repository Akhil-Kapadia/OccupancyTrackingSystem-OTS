from django.shortcuts import render, redirect
from django.db import models

# Create your views here.
import datetime as dt
from .models import Occupancy
from .forms import OccupancyForm

def home(request):
    #currentOccupancy = Occupancy.objects.latest('Time').getOccupancy()
    now = dt.datetime.now()

    currentOccupancy = 0;
    entries = Occupancy.objects.filter(Entry = True)
    exits = Occupancy.objects.filter(Entry = False)
    for people in entries:
        currentOccupancy += people.People
    for people in exits:
        currentOccupancy -= people.People


    # Form for manual entry into db.
    if (request.method == 'POST'):
        form = OccupancyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OccupancyForm


    return render(request, "home.html", context=
    {
        "currentOccupancy": currentOccupancy,
        "datetime" : now,
        'OccupancyPercentage' : currentOccupancy / 100,
        'form' : form
    })


def databaseIN(request, entry, people):
    obj = Occupancy(Entry = entry, People = people)
    obj.save()
    return redirect('home')
