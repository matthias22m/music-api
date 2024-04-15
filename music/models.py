from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    artist = models.CharField(max_length=100)
    release_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='musics')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(
        Album, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Music, related_name='playlist_songs')

    def __str__(self):
        return self.title
