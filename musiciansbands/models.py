from django.db import models
from musicians.models import Musician
from bands.models import Band


class MusicianBand(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    year_from = models.IntegerField(null=True, blank=True)
    year_to = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=48)

    def __str__(self):
        return f'{self.musician.name} - {self.musician.full_name}'