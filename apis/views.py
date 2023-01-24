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
    """Displays list of albums in json format."""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailAPIView(g.RetrieveAPIView):
    """Displays a single album details in json format."""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class BandListAPIView(g.ListAPIView):
    """Displays list of bands in json format."""
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetailAPIView(g.RetrieveAPIView):
    """Displays a single band details in json format."""
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class LabelListAPIView(g.ListAPIView):
    """Displays list of labels in json format."""
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetailAPIView(g.RetrieveAPIView):
    """Displays a single label details in json format."""
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class MusicianListAPIView(g.ListAPIView):
    """Displays list of musicians in json format."""
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailAPIView(g.RetrieveAPIView):
    """Displays a single musician details in json format."""
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class UserListAPIView(g.ListAPIView):
    """
    Displays list of users in json format.
    Only for admins.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
