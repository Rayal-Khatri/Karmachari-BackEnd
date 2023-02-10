from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'