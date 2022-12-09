from django.forms import ModelForm, DateInput
from musicians.models import Musician


class MusicianCreationForm(ModelForm):
    class Meta:
        model = Musician
        fields = [
            'name',
            'full_name',
            'born',
            'died',
            'place_of_birth',
            'bio'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['born'].widget = DateInput(attrs={"type": "date"})
        self.fields['died'].widget = DateInput(attrs={"type": "date"})
