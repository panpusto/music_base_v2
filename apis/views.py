from rest_framework import generics as g
from albums.models import Album
from bands.models import Band
from .serializers import (
    AlbumSerializer,
    BandSerializer,
)


class AlbumListAPIView(g.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailAPIView(g.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class BandListAPIView(g.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetailAPIView(g.RetrieveAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
