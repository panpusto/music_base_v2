from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    """
    Displays a form for signing up a new user.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
