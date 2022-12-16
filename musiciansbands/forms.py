from django.forms import ModelForm
from musiciansbands.models import MusicianBand


class MusicianToBandCreationForm(ModelForm):
    class Meta:
        model = MusicianBand
        fields = [
            'musician',
            'band',
            'year_from',
            'year_to',
            'role'
        ]
        