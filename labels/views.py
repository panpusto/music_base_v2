from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from labels.forms import LabelCreationForm
from django.urls import reverse_lazy


class LabelCreateView(LoginRequiredMixin, CreateView):
    form_class = LabelCreationForm
    success_url = reverse_lazy('home')
    template_name = 'labels/create_form.html'

    def form_valid(self, form):
        form.instance.added_bygi = self.request.user
        return super().form_valid(form)