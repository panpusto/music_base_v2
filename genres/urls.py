from django.urls import path

from .views import GenreCreateView

urlpatterns = [
    path('add/', GenreCreateView.as_view(), name='add_genre'),
]