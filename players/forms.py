from django import forms

from players.models import Player


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "nationality", "age", "sport", "height", "weight", "team"]
