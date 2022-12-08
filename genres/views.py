from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GenreCreationForm
from .models import Genre


class GenreCreateView(LoginRequiredMixin, CreateView):
    form_class = GenreCreationForm
    success_url = reverse_lazy('home')
    template_name = 'genres/create_form.html'
    login_url = 'account_login'


class GenreListView(ListView):
    model = Genre
    context_object_name = 'genre_list'
    template_name = 'genres/genre_list.html'
    ordering = 'name'
