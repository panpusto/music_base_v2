from django.urls import path
from albums.views import AlbumListViewAlphabetically


urlpatterns = [
    path('', AlbumListViewAlphabetically.as_view(), name='album_list_alphabetically'),
]