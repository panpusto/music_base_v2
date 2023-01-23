from rest_framework import generics as g
from rest_framework import permissions
from django.contrib.auth import get_user_model
from albums.models import Album
from bands.models import Band
from labels.models import Label
from musicians.models import Musician
from .serializers import (
    AlbumSerializer,
    BandSerializer,
    LabelSerializer,
    MusicianSerializer,
    UserSerializer
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


class LabelListAPIView(g.ListAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetailAPIView(g.RetrieveAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class MusicianListAPIView(g.ListAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailAPIView(g.RetrieveAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class UserListAPIView(g.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
