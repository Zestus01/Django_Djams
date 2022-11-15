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

    def __str__(self):
        return f"{title} is {duration} long, with {number_of_plays} plays in the {album}, done by {artists}"

class Artist(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=500)
    monthly_listeners = models.BigIntegerField(default=4200)
    grammies_won = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{name} is listened by {monthly_listeners} and won {grammies_won} grammies."

class Playlist(models.Model):
    name = models.CharField(max_length=100, default="Living in the Source Code")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
    songs = models.ManyToManyField('Song')

    def __str__(self):
        return f"{name} has {songs} on it. With the {tag}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{name}"

class Album(models.Model):
    name = models.CharField(max_length=100, default="Coder's Paradise")
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)

    def __str__(self):
        return f"{name} has {artist} on it, in the {genre} genre"

