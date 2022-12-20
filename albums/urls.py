from django.urls import path
from albums.views import AlbumListViewAlphabetically, AlbumDetailView, AlbumCreateView


urlpatterns = [
    path('', AlbumListViewAlphabetically.as_view(), name='album_list_alphabetically'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('add/', AlbumCreateView.as_view(), name='add_album'),
]