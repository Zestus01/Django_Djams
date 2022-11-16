from rest_framework import serializers
from .models import Song, Artist, Playlist, Tag, Genre, Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'explicit', 'number_of_plays', 'album', 'genre', 'artists']
