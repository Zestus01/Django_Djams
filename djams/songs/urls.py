from django.urls import path, include
from songs.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# album_list = AlbumViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# album_detail = AlbumViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = [
    # path('', include(router.urls)),
    path('songID/', song_list),
    path('songID/<int:pk>/', song_detail),
    path('tracks/', SongList.as_view()),
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>', TagDetail.as_view()),
    path('artist/', ArtistList.as_view()),
    path('artist/<int:pk>', ArtistDetail.as_view()),
    path('disco/', AlbumList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)