from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Arrival, Departure
from .forms import ArrivalForm, DepartureForm
# Create your views here.

def flights(request):
    arrivals = Arrival.objects.all()
    deapertures = Departure.objects.all()
    
    return render(request, 'flightsapp/flights.html', {'arrivals':arrivals, 'deapertures':deapertures})

@login_required
def new_arrival(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArrivalForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('flightsapp:new-arrival'))
        else:
            form = ArrivalForm()
        return render(request, 'flightsapp/new-arrival.html', {'form': form})

@login_required
def new_departure(request):
    if request.method == 'POST':
        form = DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flightsapp:new-departure'))
    else:
        form = DepartureForm()
    return render(request, 'flightsapp/new-departure.html', {'form': form})