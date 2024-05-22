from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet, PlaylistViewSet, AlbumViewSet

router = DefaultRouter()

router.register(r'music',MusicViewSet)
router.register(r'playlist',PlaylistViewSet)
router.register(r'album',AlbumViewSet)

urlpatterns = [
    path('',include(router.urls))
]