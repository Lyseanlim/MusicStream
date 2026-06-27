from django.urls import path
from .views import albums_page, album_detail

urlpatterns = [

    path(
        "",
        albums_page,
        name="albums"
    ),

    path(
        "<str:album_name>/",
        album_detail,
        name="album_detail"
    ),

]