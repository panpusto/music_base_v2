from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

LABEL_STATUS = [
    (1, 'active'),
    (2, 'closed'),
    (3, 'unknown'),
]

class Label(models.Model):
    """Representation of the music label."""
    name = models.CharField(max_length=48)
    address = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=32)
    status = models.IntegerField(choices=LABEL_STATUS)
    styles = models.CharField(max_length=128)
    founding_year = models.IntegerField()

    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns string representation of a single label object."""
        return self.name
        
    def get_absolute_url(self):
        """Gets an absolute url of single label."""
        return reverse("label_detail", args=[str(self.id)])