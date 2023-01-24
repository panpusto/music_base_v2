from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GenreCreationForm
from .models import Genre


class GenreCreateView(LoginRequiredMixin, CreateView):
    """
    Creates a genre's instace.
    Only for logged-in user.
    """
    form_class = GenreCreationForm
    success_url = reverse_lazy('home')
    template_name = 'genres/create_form.html'
    login_url = 'account_login'


class GenreListView(ListView):
    """Displays genre's list."""
    model = Genre
    context_object_name = 'genre_list'
    template_name = 'genres/genre_list.html'
    paginate_by = 10
    ordering = 'name'
