from django import forms
from .models import Icecream

class IcecreamForm(forms.ModelForm):

    class Meta:
        model = Icecream
        fields = '__all__'