from django.db import models
from django.contrib.auth.models import User
from songs.models import Song


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
