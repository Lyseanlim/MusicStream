from django.urls import path
from .views import home, browse, library, search

urlpatterns = [
    path('', home, name='home'),
    path('browse/', browse, name='browse'),
    path('library/', library, name='library'),
    path('search/', search, name='search'),
]