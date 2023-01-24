from django.contrib.auth.mixins import LoginRequiredMixin
from albums.forms import AlbumCreationForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from albums.models import Album


class AlbumCreateView(LoginRequiredMixin, CreateView):
    """
    Creates an instance of the album.
    Only for logged-in users.
    """
    form_class = AlbumCreationForm
    success_url = reverse_lazy('home')
    template_name = 'albums/create_form.html'
    login_url = 'account_login'


class AlbumListViewAlphabetically(ListView):
    """Displays list of the albums in alphabetical order."""
    model = Album
    context_object_name = 'album_list'
    template_name = 'albums/album_list_alphabetically.html'
    paginate_by = 10
    ordering = 'title'


class AlbumDetailView(DetailView):
    """Displays a single album details."""
    model = Album
    context_object_name = 'album'
    template_name = 'albums/album_detail.html'


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates an instance of the album.
    Only for logged-in users.
    """
    model = Album
    form_class = AlbumCreationForm
    success_url = reverse_lazy('album_list_alphabetically')
    template_name = 'albums/create_form.html'
