from django.db import models


class Genre(models.Model):
    """Representation of the music genre."""
    name = models.CharField(max_length=32)

    def __str__(self):
        """Returns string representation of a single genre object."""
        return self.name
