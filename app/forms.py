from django import forms
from .models import Occupancy

class AddEntry(forms.ModelForm):
    class Meta:
        model = Occupancy
        fields = "__all__"
        
