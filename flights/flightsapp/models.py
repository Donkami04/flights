from django.db import models

# Create your models here.

class Arrival(models.Model):
    flight_no = models.CharField( max_length=6)
    time = models.TimeField()
    origin = models.CharField(max_length=45)
    remarks = models.CharField(max_length=45)
    
class Departure(models.Model):
    flight_no = models.CharField(blank=False, max_length=6)
    time = models.TimeField()
    to = models.CharField(max_length=45)
    gate = models.CharField(blank=False, max_length=2)
    remarks = models.CharField(max_length=45) 
    

