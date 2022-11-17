from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets
from .models import * 
from .serializers import *
# Create your views here.

@csrf_exempt
def song_list(request):
    """
    List all Songs, or create a Song.
    """
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongIDSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SongIDSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def song_detail(request, pk):
    """
    Retrieve, update or delete a song.
    """
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SongIDSerializer(song)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = SongIDSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        song.delete()
        return HttpResponse(status=204)

class SongList(APIView):
    """
    List all songs.
    """
    def get(self, request, format=None):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagList(APIView):
    """
    List all tags
    """
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagBaseSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagBaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagDetail(APIView):
    """
    Retrieve, update or delete a tag instance.
    """
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagBaseSerializer(tag)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagBaseSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistList(APIView):
    """
    List all tags
    """
    def get(self, request, format=None):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistDetail(APIView):
    """
    Retrieve, update or delete a artist instance.
    """
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except artist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        artist = self.get_object(pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbumList(APIView):
    """
    List all tags
    """
    def get(self, request, format=None):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset is for displaying album querysets
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]

    ##@action(detail=True, renderer_class=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        print('request')
        print(request.user)
        serializer.save()
        



