from rest_framework import serializers
from .models import Song, Artist, Playlist, Tag, Genre, Album

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    class Meta:
        model = Album
        fields = ['id', 'name', 'tag']

class SongIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'explicit', 'number_of_plays', 'album', 'genre', 'artist']


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    genre = GenreSerializer()
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Song
        fields = ['id', 'title', 'explicit', 'number_of_plays', 'album', 'genre', 'artist']

class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    genre = GenreSerializer()
    tag = TagSerializer()
    
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'genre', 'tag', 'songs']