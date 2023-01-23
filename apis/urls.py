from django.urls import path
import apis.views as v

urlpatterns = [
    # albums
    path('albums/', v.AlbumListAPIView.as_view(), name='api_albums_list'),
    path('albums/<int:pk>/', v.AlbumDetailAPIView.as_view(), name='api_album_detail'),
    # bands
    path('bands/', v.BandListAPIView.as_view(), name='api_bands_list'),
    path('bands/<int:pk>/', v.BandDetailAPIView.as_view(), name='api_band_detail'),
]
