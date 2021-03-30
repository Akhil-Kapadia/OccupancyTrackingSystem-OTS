from django import forms
from .models import Occupancy

class OccupancyForm(forms.ModelForm):
    class Meta:
        model = Occupancy
        fields = [
            'Entry',
            'People'
        ]

class Doors(forms.Form):
    CHOCIES = (
        ('OPEN', 'Open Doors'),
        ('CLOSE', 'Close Doors'),
        ('RESET', 'Reset Doors')
    )
    doors = forms.ChoiceField(choices=CHOCIES)
        