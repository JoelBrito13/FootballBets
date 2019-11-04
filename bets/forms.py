from django import forms

from .models import Bet
from games.models import Game

class CreateBet(forms.Form):
    user = forms.IntegerField
    game = forms.IntegerField
    amount = forms.FloatField

