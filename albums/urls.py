from django.urls import path
from albums.views import AlbumListViewAlphabetically, AlbumDetailView


urlpatterns = [
    path('', AlbumListViewAlphabetically.as_view(), name='album_list_alphabetically'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
]