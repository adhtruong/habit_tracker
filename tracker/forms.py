from django import forms
from .models import Run

class RunForm(forms.ModelForm):
    units = forms.ChoiceField(choices=("km","miles"))

    class Meta:
        model = Run
        fields = ['date', 'distance', 'time', 'description']
