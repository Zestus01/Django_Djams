from django.contrib import admin
from .models import Tag, Song, Artist, Genre, Album, Playlist

# Register your models here.
admin.site.register(Tag)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Playlist)