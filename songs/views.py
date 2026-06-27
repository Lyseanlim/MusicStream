from django.shortcuts import render, get_object_or_404
from .models import Song, RecentlyPlayed
from playlists.models import Playlist


def song_detail(request, song_id):

    song = get_object_or_404(
        Song,
        id=song_id
    )

    previous_song = (
        Song.objects.filter(id__lt=song.id)
        .order_by("-id")
        .first()
    )

    next_song = (
        Song.objects.filter(id__gt=song.id)
        .order_by("id")
        .first()
    )

    playlists = []

    if request.user.is_authenticated:

        playlists = Playlist.objects.filter(
            user=request.user
        )

        recently_played, created = RecentlyPlayed.objects.get_or_create(
            user=request.user,
            song=song
        )

        if not created:
            recently_played.save()

    return render(
        request,
        "songs/detail.html",
        {
            "song": song,
            "previous_song": previous_song,
            "next_song": next_song,
            "playlists": playlists,
        }
    )