from django.db import models
from genres.models import Genre
from labels.models import Label
from musicians.models import Musician
from django.contrib.auth import get_user_model
from django.urls import reverse


BAND_STATUS = [
    (1, 'active'),
    (2, 'on hold'),
    (3, 'split-up'),
    (4, 'unknown'),
    (5, 'changed name'),
    (6, 'disputed'),
]


class Band(models.Model):
    """Representation of the music band."""
    name = models.CharField(max_length=64)
    country_of_origin = models.CharField(max_length=32)
    location = models.CharField(max_length=48)
    status = models.IntegerField(choices=BAND_STATUS)
    formed_in = models.IntegerField()
    ended_in = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    lyrical_themes = models.CharField(max_length=64)
    current_label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name='current_label'
    )
    bio = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(
        Musician,
        through='musiciansbands.MusicianBand'
    )

    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns string representation of band object."""
        return f'{self.name}, {self.country_of_origin}'

    def get_absolute_url(self):
        """Gets an absolute url of single band."""
        return reverse("band_detail", args=[str(self.id)])