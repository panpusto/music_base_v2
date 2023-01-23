from rest_framework import generics as g
from albums.models import Album
from .serializers import AlbumSerializer


class AlbumListAPIView(g.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailAPIView(g.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer