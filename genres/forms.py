from django.forms import ModelForm
from genres.models import Genre


class GenreCreationForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
