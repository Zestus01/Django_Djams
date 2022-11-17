from django.urls import path
from songs import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('song/', views.song_list),
    path('song/<int:pk>/', views.song_detail),
    path('tracks/', views.SongList.as_view()),
    path('tag/', views.TagList.as_view()),
    path('tag/<int:pk>', views.TagDetail.as_view()),
    path('artist/', views.ArtistList.as_view()),
    path('artist/<int:pk>', views.ArtistDetail.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)