from django.urls import path
from bands.views import (
    BandCreateView,
    BandListViewAlphabetically,
    BandDetailView,
    BandUpdateView
)


urlpatterns = [
    path('', BandListViewAlphabetically.as_view(), name='band_list_alphabetically'),
    path('<int:pk>/', BandDetailView.as_view(), name='band_detail'),
    path('add/', BandCreateView.as_view(), name='add_band'),
    path('update/<int:pk>/', BandUpdateView.as_view(), name='band_update'),
]
