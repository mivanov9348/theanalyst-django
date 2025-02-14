from django import forms
from .models import Athlete

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ["first_name", "last_name", "nationality", "age", "sport", "height", "weight", "team"]
