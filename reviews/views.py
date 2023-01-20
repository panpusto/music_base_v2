from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from reviews.forms import ReviewCreationForm
from django.urls import reverse_lazy
from reviews.models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    form_class = ReviewCreationForm
    success_url = reverse_lazy('home')
    template_name = 'reviews/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewListView(ListView):
    model = Review
    context_object_name = 'review_list'
    template_name = 'reviews/review_list.html'
    paginate_by = 10
    ordering = 'added'


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'reviews/review_detail.html'


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewCreationForm
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/create_form.html'


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/confirm_delete.html'
