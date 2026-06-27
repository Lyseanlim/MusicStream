from django.db import models
from django.contrib.auth.models import User
from songs.models import Song

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.song.title}"
