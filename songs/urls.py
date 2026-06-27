from django.urls import path
from .views import song_detail

urlpatterns = [
    path('<int:song_id>/', song_detail, name='song_detail'),
]