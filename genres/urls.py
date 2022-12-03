from django.urls import path
from .views import GenreCreateView, GenreListView

urlpatterns = [
    path('', GenreListView.as_view(), name='genre_list'),
    path('add/', GenreCreateView.as_view(), name='add_genre'),
]