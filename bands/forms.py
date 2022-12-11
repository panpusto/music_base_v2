from django.forms import ModelForm
from bands.models import Band


class BandCreationForm(ModelForm):
    class Meta:
        model = Band
        fields = [
            'name',
            'country_of_origin',
            'location',
            'status',
            'formed_in',
            'ended_in',
            'genre',
            'lyrical_themes',
            'current_label',
            'bio',
        ]
        