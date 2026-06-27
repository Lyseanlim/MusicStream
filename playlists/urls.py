from django.urls import path
from .views import (
    playlists_page,
    create_playlist,
    playlist_detail,
    add_song_to_playlist,
    remove_song_from_playlist,
    delete_playlist,
)

urlpatterns = [

    path(
        "",
        playlists_page,
        name="playlists"
    ),

    path(
        "create/",
        create_playlist,
        name="create_playlist"
    ),

    path(
        "<int:playlist_id>/",
        playlist_detail,
        name="playlist_detail"
    ),

    path(
        "<int:playlist_id>/add/<int:song_id>/",
        add_song_to_playlist,
        name="add_song_to_playlist"
    ),

    path(
        "<int:playlist_id>/remove/<int:song_id>/",
        remove_song_from_playlist,
        name="remove_song_from_playlist"
    ),

    path(
        "<int:playlist_id>/delete/",
        delete_playlist,
        name="delete_playlist"
    ),

]