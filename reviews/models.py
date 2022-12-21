from django.db import models
from albums.models import Album
from bands.models import Band
from django.contrib.auth import get_user_model


class Review(models.Model):
    subject = models.CharField(max_length=32)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    added = models.DateTimeField(auto_now_add=True)