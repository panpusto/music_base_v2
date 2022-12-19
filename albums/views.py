from django.views.generic import ListView
from albums.models import Album


class AlbumListViewAlphabetically(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'albums/album_list_alphabetically.html'
    ordering = 'title'