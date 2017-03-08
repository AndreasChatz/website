from django.db import models

# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length=40)
	album_title = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album_logo = models.CharField(max_length=250)

	def __str__(self):
		return self.artist + '-' + self.album_title


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=5)
	song_title = models.CharField(max_length=250)
