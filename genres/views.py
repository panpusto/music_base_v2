from django.urls import reverse_lazy
from django.views import generic
from .forms import GenreCreationForm

class GenreCreateView(generic.CreateView):
    form_class = GenreCreationForm
    success_url = reverse_lazy('home')
    template_name = 'genres/create_form.html'