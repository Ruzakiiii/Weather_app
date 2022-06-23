from .models import CITY
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = CITY
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name':'city',
            'id':'city',
            'placeholder':'Введите город'
        })}