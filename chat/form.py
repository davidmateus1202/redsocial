# forms.py

from django import forms
from .models import creaRoom

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = creaRoom
        fields = ['name', 'description']