from django.urls import path
import apis.views as v

urlpatterns = [
    # albums
    path(
        'albums/',
        v.AlbumListAPIView.as_view(),
        name='api_albums_list'),
    path(
        'albums/<int:pk>/',
        v.AlbumDetailAPIView.as_view(),
        name='api_album_detail'),
    # bands
    path(
        'bands/',
        v.BandListAPIView.as_view(),
        name='api_bands_list'),
    path(
        'bands/<int:pk>/',
        v.BandDetailAPIView.as_view(),
        name='api_band_detail'),
    # labels
    path(
        'labels/',
        v.LabelListAPIView.as_view(),
        name='api_labels_list'),
    path(
        'labels/<int:pk>/',
        v.LabelDetailAPIView.as_view(),
        name='api_label_detail'),
    # musicians
    path(
        'musicians/',
        v.MusicianListAPIView.as_view(),
        name='api_musicians_list'),
    path(
        'musicians/<int:pk>/',
        v.MusicianDetailAPIView.as_view(),
        name='api_musician_detail'),
    # users
    path(
        'users/',
        v.UserListAPIView.as_view(),
        name='api_user_list'),
]
