from django.forms import ModelForm
from .models import Plans


class CreatePlanForm(ModelForm):
    class Meta:
        model = Plans
        fields = [
            'title',
            'stand_url',
            'stand_user',
            'species',
            'process',
            'text',
        ]
