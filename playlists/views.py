from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Playlist
from songs.models import Song


@login_required(login_url="login")
def playlists_page(request):

    playlists = Playlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        "playlists/playlists.html",
        {
            "playlists": playlists
        }
    )


@login_required(login_url="login")
def create_playlist(request):

    if request.method == "POST":

        name = request.POST["name"]

        Playlist.objects.create(
            user=request.user,
            name=name
        )

        return redirect("playlists")

    return render(
        request,
        "playlists/create_playlist.html"
    )


@login_required(login_url="login")
def playlist_detail(request, playlist_id):

    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        user=request.user
    )

    return render(
        request,
        "playlists/detail.html",
        {
            "playlist": playlist
        }
    )


@login_required(login_url="login")
def add_song_to_playlist(request, playlist_id, song_id):

    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        user=request.user
    )

    song = get_object_or_404(
        Song,
        id=song_id
    )

    playlist.songs.add(song)

    return redirect(
        "playlist_detail",
        playlist_id=playlist.id
    )


@login_required(login_url="login")
def remove_song_from_playlist(request, playlist_id, song_id):

    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        user=request.user
    )

    song = get_object_or_404(
        Song,
        id=song_id
    )

    playlist.songs.remove(song)

    return redirect(
        "playlist_detail",
        playlist_id=playlist.id
    )


@login_required(login_url="login")
def delete_playlist(request, playlist_id):

    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        user=request.user
    )

    playlist.delete()

    return redirect("playlists")