from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from reviews.forms import ReviewCreationForm
from django.urls import reverse_lazy


class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewCreationForm
    success_url = reverse_lazy('home')
    template_name = 'reviews/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)