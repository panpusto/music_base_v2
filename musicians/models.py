from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Musician(models.Model):
    name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=64)
    born = models.DateField(blank=True)
    died = models.DateField(blank=True)
    place_of_birth = models.CharField(max_length=32)
    bio = models.TextField(blank=True)

    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.full_name}'

    def get_absolute_url(self):
        return reverse("musician_detail", args=[str(self.id)])