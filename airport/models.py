from django.db import models

class Airport(models.Model):
    iata = models.CharField(max_length=3)
    city = models.CharField(max_length=100)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    obs = models.CharField(max_length=256, blank=True) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.iata
