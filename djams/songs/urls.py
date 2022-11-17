from django.urls import path
from songs.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

album_list = AlbumViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

album_detail = AlbumViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('songID/', song_list),
    path('songID/<int:pk>/', song_detail),
    path('tracks/', SongList.as_view()),
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>', TagDetail.as_view()),
    path('artist/', ArtistList.as_view()),
    path('artist/<int:pk>', ArtistDetail.as_view()),
    path('album/', album_list, name='album-list'),
    path('album/<int:pk>/', album_detail, name='album-detail')


]

urlpatterns = format_suffix_patterns(urlpatterns)