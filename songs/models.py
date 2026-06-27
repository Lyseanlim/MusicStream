from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

    audio_file = models.FileField(upload_to="songs/")
    cover_image = models.ImageField(upload_to="covers/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecentlyPlayed(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE
    )

    played_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-played_at"]

    def __str__(self):
        return f"{self.user.username} - {self.song.title}"