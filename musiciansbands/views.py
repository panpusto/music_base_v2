from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from musiciansbands.forms import MusicianToBandCreationForm
from django.urls import reverse_lazy


class MusicianToBandCreateView(LoginRequiredMixin, CreateView):
    """
    Creates an instance of the band member.
    Only for logged-in user.
    """
    form_class = MusicianToBandCreationForm
    success_url = reverse_lazy('home')
    template_name = 'musiciansbands/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        """Adds logged-in user as an author."""
        form.instance.added_by = self.request.user
        return super().form_valid(form)
        