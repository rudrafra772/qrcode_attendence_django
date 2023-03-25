from django import forms
from .models import Attendenc

class AttendenceForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Attendenc
        fields = ['name']
