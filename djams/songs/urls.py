from django.urls import path
from songs import views

urlpatterns = [
    path('song/', views.song_list),
    path('song/<int:pk>/', views.song_detail)
]