from django.shortcuts import render
from django.db.models import Q
from songs.models import Song, RecentlyPlayed
from favorites.models import Favorite


def home(request):

    recently_added = Song.objects.all().order_by("-created_at")[:6]

    recently_played = []

    favorite_songs = []

    if request.user.is_authenticated:

        recently_played = RecentlyPlayed.objects.filter(
            user=request.user
        )[:6]

        favorite_songs = Favorite.objects.filter(
            user=request.user
        )[:6]

    return render(
        request,
        "home.html",
        {
            "songs": recently_added,
            "recently_played": recently_played,
            "favorite_songs": favorite_songs,
        }
    )


def library(request):

    return render(
        request,
        "library.html"
    )


def search(request):

    query = request.GET.get("q", "").strip()

    songs = Song.objects.all()

    if query:

        songs = Song.objects.filter(

            Q(title__icontains=query) |

            Q(artist__icontains=query) |

            Q(album__icontains=query)

        ).distinct()

    return render(
        request,
        "search.html",
        {
            "songs": songs,
            "query": query
        }
    )


def browse(request):

    trending_songs = Song.objects.all().order_by("?")[:6]

    new_releases = Song.objects.all().order_by("-created_at")[:6]

    return render(
        request,
        "browse.html",
        {
            "trending_songs": trending_songs,
            "new_releases": new_releases
        }
    )