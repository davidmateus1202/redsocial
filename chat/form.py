# forms.py

from django import forms
from .models import *

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']