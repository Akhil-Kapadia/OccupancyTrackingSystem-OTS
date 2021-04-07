from django import forms
from .models import Occupancy, Doors

class OccupancyForm(forms.ModelForm):
    class Meta:
        model = Occupancy
        fields = [
            'Entry',
            'People'
        ]

class DoorForm(forms.ModelForm):
    class Meta:
        model = Doors
        fields = [
            'status'
        ]
        