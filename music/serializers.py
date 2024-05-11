from rest_framework import serializers
from .models import Music, Album, Playlist


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id',"title", "artist", "release_date"]
    
    
    
class MusicSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(
        queryset = Album.objects.all(),
        many = False
    )
    
    class Meta:
        model = Music
        fields = ["title", "artist", "duration",
                  "audio_file", "posted_by", "album"]


class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(
        queryset=Music.objects.all(),
        many=True
    )

    class Meta:
        model = Playlist
        fields = ["title", "description", "created_by", "songs"]
    
    def create(self, validated_data):
        related_songs = validated_data.pop('songs') 
        playlist = Playlist.objects.create(**validated_data) 

        for song in related_songs:
            playlist.songs.add(song)

        return playlist