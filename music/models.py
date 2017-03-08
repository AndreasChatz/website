from django.db import models

# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length=40)
	album_title = modles.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album_logo = models.CharField(max_length=250)
	