from django.db import models


# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=80)
    duration = models.FloatField()
    explicit = models.BooleanField(default=False)
    number_of_plays = models.BigIntegerField(blank=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    artists = models.ManyToManyField('Artist')

class Artist(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=500)
    monthly_listeners = models.BigIntegerField(default=4200)
    grammies_won = models.SmallIntegerField(default=0, blank=True)

class Playlist(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
    songs = models.ManyToManyField('Song')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)