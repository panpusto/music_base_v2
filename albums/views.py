from django.contrib.auth.mixins import LoginRequiredMixin
from albums.forms import AlbumCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from albums.models import Album


class AlbumCreateView(LoginRequiredMixin, CreateView):
    form_class = AlbumCreationForm
    success_url = reverse_lazy('home')
    template_name = 'albums/create_form.html'
    login_url = 'account_login'


class AlbumListViewAlphabetically(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'albums/album_list_alphabetically.html'
    ordering = 'title'


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'albums/album_detail.html'
