from django.urls import path
from musicians.views import (
    MusicianListView,
    MusicianCreateView,
    MusicianDetailView,
    MusicianUpdateView
)


urlpatterns = [
    path('', MusicianListView.as_view(), name='musician_list'),
    path('add/', MusicianCreateView.as_view(), name='add_musician'),
    path('<int:pk>/', MusicianDetailView.as_view(), name='musician_detail'),
    path('update/<int:pk>/', MusicianUpdateView.as_view(), name='musician_update'),
]
