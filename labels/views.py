from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from labels.forms import LabelCreationForm
from django.urls import reverse_lazy
from labels.models import Label

class LabelCreateView(LoginRequiredMixin, CreateView):
    form_class = LabelCreationForm
    success_url = reverse_lazy('home')
    template_name = 'labels/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)


class LabelListView(ListView):
    model = Label
    context_object_name = 'label_list'
    template_name = 'labels/label_list.html'
    ordering = 'name'
    

class LabelDetailView(DetailView):
    model = Label
    context_object_name = 'label'
    template_name = 'labels/label_detail.html'