from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorite
from songs.models import Song


@login_required(login_url="login")
def favorites_page(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    return render(
        request,
        "favorites/favorites.html",
        {
            "favorites": favorites
        }
    )


@login_required(login_url="login")
def add_favorite(request, song_id):

    song = get_object_or_404(
        Song,
        id=song_id
    )

    Favorite.objects.get_or_create(
        user=request.user,
        song=song
    )

    return redirect(
        "song_detail",
        song_id=song.id
    )


@login_required(login_url="login")
def remove_favorite(request, song_id):

    song = get_object_or_404(
        Song,
        id=song_id
    )

    Favorite.objects.filter(
        user=request.user,
        song=song
    ).delete()

    return redirect("favorites")