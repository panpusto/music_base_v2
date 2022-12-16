from django.urls import path
from musiciansbands.views import MusicianToBandCreateView


urlpatterns = [
    path('add/', MusicianToBandCreateView.as_view(), name='add_musician_to_band')
]
