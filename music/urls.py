from django.urls import path
from . import views

urlpatterns = [
    path('musics/',views.music_list),
    path('musics/<int:id>/',views.music_detail),
    path('playlists/',views.playlist_list),
    path('playlists/<int:id>/',views.playlist_detail),
]
