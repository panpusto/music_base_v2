from django.forms import ModelForm
from labels.models import Label

class LabelCreationForm(ModelForm):
    class Meta:
        model = Label
        fields = [
            'name',
            'address',
            'country',
            'status',
            'styles',
            'founding_year'
        ]
