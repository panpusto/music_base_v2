from django.forms import ModelForm, NumberInput
from reviews.models import Review


class ReviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'subject',
            'album',
            'band',
            'rating',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget = NumberInput(
            attrs={
                'step': 0.5,
                 'min': 0,
                  'max': 10
                  })
