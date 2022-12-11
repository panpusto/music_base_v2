from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from bands.forms import BandCreationForm
from django.urls import reverse_lazy
from bands.models import Band


class BandCreateView(LoginRequiredMixin, CreateView):
    form_class = BandCreationForm
    success_url = reverse_lazy('home')
    template_name = 'bands/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class BandListViewAlphabetically(ListView):
    model = Band
    context_object_name = 'band_list'
    template_name = 'bands/band_list_alphabetically.html'
    ordering = 'name'