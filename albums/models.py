from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from bands.models import Band
from genres.models import Genre
from labels.models import Label


ALBUM_TYPES = [
    (1, 'Full-length'),
    (2, 'EP/Mini-albums'),
    (3, 'Compilation'),
    (4, 'Single'),
    (5, 'Mixtape'),
    (6, 'DJ Mix'),
    (7, 'Bootleg/Unauthorized'),
    (8, 'Live album'),
    (9, 'Video'),
    (10, 'Soundtrack'),
    (11, 'Promo'),
]


FORMAT_TYPES = [
    (1, 'CD'),
    (2, 'vinyl'),
    (3, 'cassette'),
    (4, 'CD/DVD'),
    (5, 'digibook'),
    (6, 'digital'),
    (7, 'all formats'),
]


class Album(models.Model):
    title = models.CharField(max_length=64)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='album_by')
    genre = models.ManyToManyField(Genre)
    album_type = models.IntegerField(choices=ALBUM_TYPES)
    release_date = models.DateField(null=True)
    catalog_id = models.CharField(max_length=16)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    album_format = models.IntegerField(choices=FORMAT_TYPES)
    cover = models.ImageField(upload_to='album_covers/')

    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.band}'

    def get_absolute_url(self):
        return reverse("album_detail", args=[str(self.id)])
        