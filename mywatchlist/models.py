from django.db import models

# Create your models here.

class MyWatchlist(models.Model):
    watched = models.CharField(max_length=50) 
    title = models.CharField(max_length=50) 
    rating = models.FloatField() # angka 
    release_date = models.CharField(max_length=50) # string
    review = models.TextField() # string vers panjang