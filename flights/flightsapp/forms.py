from django import forms
from .models import Arrival, Departure

class ArrivalForm(forms.ModelForm):
    class Meta:
        model = Arrival
        fields = ['time', 'origin', 'flight_no', 'remarks']
        
        
class DepartureForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = ['time', 'to', 'flight_no', 'gate', 'remarks']
