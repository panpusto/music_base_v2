from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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
    """
    Creates an instance of review.
    Only for logged-in user.
    """
    form_class = ReviewCreationForm
    success_url = reverse_lazy('home')
    template_name = 'reviews/create_form.html'
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewListView(ListView):
    """Displays a list of the reviews."""
    model = Review
    context_object_name = 'review_list'
    template_name = 'reviews/review_list.html'
    paginate_by = 10
    ordering = 'added'


class ReviewDetailView(DetailView):
    """Displays a single review details."""
    model = Review
    context_object_name = 'review'
    template_name = 'reviews/review_detail.html'


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates an instance of the review.
    Only for logged-in author of the review.
    """
    model = Review
    form_class = ReviewCreationForm
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/create_form.html'

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deletes an instance of the review.
    Only for logged-in author of the review.
    """
    model = Review
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/confirm_delete.html'

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj
