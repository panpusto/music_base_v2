from django.forms import ModelForm
from albums.models import Album


class AlbumCreationForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'band',
            'genre',
            'album_type',
            'release_date',
            'catalog_id',
            'label',
            'album_format',
            'cover']
