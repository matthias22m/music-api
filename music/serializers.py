from rest_framework import serializers
from .models import Music

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["title", "artist", "release_date"]

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["title", "artist", "duration", "audio_file", "posted_by", "album"]

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["title", "description", "created_by", "song"]