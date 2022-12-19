from django.views.generic import ListView, DetailView
from albums.models import Album


class AlbumListViewAlphabetically(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'albums/album_list_alphabetically.html'
    ordering = 'title'


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'albums/album_detail.html'
