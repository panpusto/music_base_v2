from django.urls import path
import apis.views as v

urlpatterns = [
    # albums
    path('albums/', v.AlbumListAPIView.as_view(), name='api_albums_list'),
    path('albums/<int:pk>/', v.AlbumDetailAPIView.as_view(), name='api_albums_detail'),
]