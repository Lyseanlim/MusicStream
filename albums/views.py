from django.shortcuts import render, get_object_or_404
from songs.models import Song


def albums_page(request):

    all_songs = Song.objects.order_by("album", "id")

    albums = []
    seen_albums = set()

    for song in all_songs:
        if song.album not in seen_albums:
            albums.append(song)
            seen_albums.add(song.album)

    return render(
        request,
        "albums/albums.html",
        {
            "albums": albums
        }
    )


def album_detail(request, album_name):

    songs = Song.objects.filter(
        album=album_name
    )

    album = songs.first()

    return render(
        request,
        "albums/detail.html",
        {
            "album": album,
            "songs": songs
        }
    )

    return render(
        request,
        "albums/detail.html",
        {
            "album": album,
            "songs": songs
        }
    )