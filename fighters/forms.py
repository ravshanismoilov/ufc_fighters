from django.forms import ModelForm
from .models import Fighter


class CreateFighterForm(ModelForm):
    class Meta:
        model = Fighter
        fields = '__all__'

        