from django.forms.fields import NullBooleanField
from django.shortcuts import render, redirect
from django.db import models

# Create your views here.
import datetime as dt
from .models import Occupancy, Doors
from .forms import OccupancyForm, DoorForm


def home(request):
    now = dt.datetime.now()

    currentOccupancy = 0;
    entries = Occupancy.objects.filter(Entry = True)
    exits = Occupancy.objects.filter(Entry = False)
    for people in entries:
        currentOccupancy += people.People
    for people in exits:
        currentOccupancy -= people.People
    
    percentage = currentOccupancy/17 * 100

    doorstatus = Doors.objects.latest().status
    if doorstatus == 'RESET':
        door = 'OPEN' if percentage < 99 else 'CLOSE'
        print('EDS controlled by WebApp System')
    else:
        door = doorstatus
        print('EDS controlled by User')
        
        
       
    

    # Form for manual entry into db.
    if (request.method == 'POST'):
        doors = DoorForm(request.POST)
        form = OccupancyForm(request.POST)

        if doors.is_valid():
            doors.save()
            return redirect('home')
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        doors = DoorForm
        form = OccupancyForm
    
    
    

    return render(request, "home.html", context=
    {
        "currentOccupancy": currentOccupancy,
        "datetime" : now,
        'OccupancyPercentage' : percentage,
        'door' : door,
        'doors' : doors,
        'form' : form
    })


def databaseIN(request, entry, people):
    obj = Occupancy(Entry = entry, People = people)
    obj.save()
    return redirect('home')

