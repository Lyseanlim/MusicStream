from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

    # Store the MP3 and cover image in Cloudinary
    audio_file = CloudinaryField(
        resource_type="video"
    )

    cover_image = CloudinaryField(
        "image"
    )

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