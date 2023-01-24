from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "flightsapp"

urlpatterns = [
    path('flights/', views.flights, name='home'),
    path('login/', LoginView.as_view(template_name='flightsapp/login.html'), name='login'),
    path('new-arrival/', views.new_arrival, name='new-arrival'),
    path('new-departure/', views.new_departure, name='new-departure'),
]