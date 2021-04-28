# Create your views here.

from django.db import models
from django.forms.fields import NullBooleanField
from django.shortcuts import redirect, render
#math
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statistics import NormalDist
import datetime as dt
import numpy as np
import pandas as pd

from .forms import DoorForm, OccupancyForm
from .models import Doors, Occupancy
from django.http import HttpResponse


def home(request):
    # Get current Occuancy and max %
    now = dt.datetime.now()
    currentOccupancy = 0;
    entries = Occupancy.objects.filter(Entry = True)
    exits = Occupancy.objects.filter(Entry = False)
    for people in entries:
        currentOccupancy += people.People
    for people in exits:
        currentOccupancy -= people.People
    percentage = currentOccupancy/17 * 100

    # Check door status
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

def confidence_interval(data, confidence=0.95):
  dist = NormalDist.from_samples(data)
  z = NormalDist().inv_cdf((1 + confidence) / 2.)
  h = dist.stdev * z / ((len(data) - 1) ** .5)
  return dist.mean - h, dist.mean + h

#to access this page add /graph to end of url
def graph(request):
    #getting data from db
    test = []
    samples = 0
    y = [0]*24
    occ = 0
    obj = Occupancy.objects.latest()
    i = obj.pk
    while(samples < 1000):
        try:
            db = Occupancy.objects.get(pk=i)    #Get DB entry if it exists
        except:
            break
        i -= 1
        today = dt.datetime.now()   #Get current day
        #See if this DB entry matches today ie Tuesday = Tuesday
        if db.TimeStamp.strftime("%w") != today.strftime("%w"):
            continue
        else:   #Do statistics here
            if db.Entry:
                y[db.TimeStamp.hour] +=  db.People  # Add to hr people entered

            else:
                y[db.TimeStamp.hour] -=  db.People  # Sub to hr people exited
            samples += 1
    #Math
    x = [i for i in range(0,24)]
    for i, hr in enumerate(y):
        occ += hr
        y[i] = np.abs(occ)

    Upper, Lower = confidence_interval(y)

    # Graphing
    graph = go.Figure(go.Bar(x=x, y=y, name="Todays Occupancy", error_y = dict(
        type = 'percent',
        symmetric = False,
        value = Upper,
        valueminus = Lower
    )))
    graph.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 1,
            dtick = 1
        ),
        title = 'Today\'s Occupancy',
        xaxis_title = 'Hour (UTC Military Time)',
        yaxis_title = 'Occupancy'
    )
    
    # Setting layout of the figure.
    layout = {
        'title': 'Today\'s Occupancy',
        'xaxis_title': 'Hour (UTC Military Time)',
        'yaxis_title': 'Occupancy',
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graph, 'layout': layout}, 
                    output_type='div')
    # plot_div = y
    #You can change plot_div to test to check the graph, just make sure to fix demo-plot.html
    return render(request, 'Occupancy Graph.html', 
                  context={'plot_div': plot_div})
