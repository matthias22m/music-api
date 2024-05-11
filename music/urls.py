from django.urls import path
from . import views

urlpatterns = [
    path('musics/',views.music_list),
    path('musics/<int:id>/',views.music_detail),
    path('playlists/',views.playlist_list),
    path('playlists/<int:id>/',views.playlist_detail),
    path('albums/',views.album_list),
    path('albums/<int:id>/',views.album_detail),
]
