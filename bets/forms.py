from django import forms

from .models import Bet
from games.models import Game

class CreateBet(forms.Form):
    user = forms.IntegerField
    game = forms.IntegerField
    amount = forms.FloatField

class DeleteForm(forms.Form):
    bet_id_del = forms.IntegerField(label='Bets')

class ChangeBet(forms.Form):
    user = forms.IntegerField
    game = forms.IntegerField
    amount = forms.FloatField
