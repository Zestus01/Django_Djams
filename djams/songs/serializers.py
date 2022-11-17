from rest_framework import serializers
from .models import Song, Artist, Playlist, Tag, Genre, Album
    

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class TagBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    tag = TagBaseSerializer()
    class Meta:
        model = Album
        fields = [
                    'id', 
                    'name', 
                    'tag',
                ]
    # def create(self, validated_data):
    #     tags = validated_data.pop('tag')
    #     album_instance = Album.objects.create(**validated_data)
    #     for tag in tags:
    #         Tag.objects.create(name=album_instance)
    #     return Album(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Tag = validated_data.get('Tag', instance.Tag)
        instance.save()
        return instance
    
class TagSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    class Meta:
        model = Tag
        fields = "__all__"

    def create(self, validated_data):
        album = validated_data.pop('album')
        tag_instance = Tag.objects.create(**validated_data)
        for album in albums:
            Album.objects.create(tag=tag_instance)
        return tag_instance   

class SongIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
                    'id', 
                    'title', 
                    'explicit', 
                    'number_of_plays', 
                    'album', 
                    'genre', 
                    'artist',
                ]


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    genre = GenreSerializer()
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Song
        fields = [
                    'id', 
                    'title', 
                    'explicit', 
                    'number_of_plays', 
                    'album', 
                    'genre', 
                    'artist',
                ]

class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    genre = GenreSerializer()
    tag = TagSerializer()
    
    class Meta:
        model = Playlist
        fields = [
                    'id', 
                    'name', 
                    'genre', 
                    'tag', 
                    'songs',
                ]