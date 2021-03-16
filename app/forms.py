from django import forms
from .models import Occupancy

class OccupancyForm(forms.ModelForm):
    class Meta:
        model = Occupancy
        fields = [
            'Entry',
            'People',
            'CurrentOccupancy'
        ]
        