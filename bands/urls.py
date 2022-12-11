from django.urls import path
from bands.views import BandCreateView, BandListViewAlphabetically


urlpatterns = [
    path('', BandListViewAlphabetically.as_view(), name='band_list_alphabetically'),
    path('add/', BandCreateView.as_view(), name='add_band'),
]
