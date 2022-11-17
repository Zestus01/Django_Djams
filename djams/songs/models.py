from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

### Vaidators Created Here
def validate_positive(value):
        if (value < 0):
            raise ValidationError(
                _('%(value)s is not a valid input'),
                params={'value', value},
            )

class Song(models.Model):
    title = models.CharField(max_length=80)
    duration = models.FloatField(default=210)
    explicit = models.BooleanField(default=False)
    number_of_plays = models.BigIntegerField(validators=[MinValueValidator(0)], blank=False)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    artist = models.ManyToManyField('Artist')

    def __str__(self):
        return f"{self.title} plays in the {self.album}, done by {self.artists}"

class Artist(models.Model):
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    monthly_listeners = models.BigIntegerField(default=4200)
    grammies_won = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0, blank=True)


    def __str__(self):
        return f"{self.name}."

class Playlist(models.Model):
    name = models.CharField(max_length=100, default="Living in the Source Code")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT)
    songs = models.ManyToManyField('Song')

    def __str__(self):
        return f"{self.name} has {self.songs} on it. With the {self.tag}"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Album(models.Model):
    name = models.CharField(max_length=100, default="Coder's Paradise")
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"{self.name}, in the {self.tag} genre"

