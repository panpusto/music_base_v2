from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Musician(models.Model):
    """Representation of the musician."""
    name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=64)
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=32)
    bio = models.TextField(blank=True)

    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the single musician object."""
        return f'{self.name} - {self.full_name}'

    def get_absolute_url(self):
        """Gets absolute url of a single musician."""
        return reverse("musician_detail", args=[str(self.id)])