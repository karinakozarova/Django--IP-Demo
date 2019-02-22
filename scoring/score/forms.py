from django import forms
from django.forms import ModelForm

from .models import Score


class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = [
            'left_player_score',
            'right_player_score',
        ]
