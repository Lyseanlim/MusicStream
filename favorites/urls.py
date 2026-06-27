from django.urls import path
from .views import (
    favorites_page,
    add_favorite,
    remove_favorite,
)

urlpatterns = [

    path(
        "",
        favorites_page,
        name="favorites"
    ),

    path(
        "add/<int:song_id>/",
        add_favorite,
        name="add_favorite"
    ),

    path(
        "remove/<int:song_id>/",
        remove_favorite,
        name="remove_favorite"
    ),

]