from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from musicians.forms import MusicianCreationForm
from django.urls import reverse_lazy
from musicians.models import Musician


class MusicianCreateView(LoginRequiredMixin, CreateView):
    form_class = MusicianCreationForm
    success_url = reverse_lazy('home')
    template_name = 'musicians/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
        

class MusicianListView(ListView):
    model = Musician
    context_object_name = 'musician_list'
    template_name = 'musicians/musician_list.html'
    paginate_by = 10
    ordering = 'name'


class MusicianDetailView(DetailView):
    model = Musician
    context_object_name = 'musician'
    template_name = 'musicians/musician_detail.html'
