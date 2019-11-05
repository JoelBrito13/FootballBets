from django import forms


class SearchGame(forms.Form):
    search = forms.CharField(label='Search game', max_length=100)


class SearchParam(forms.Form):
    # league_id = forms.CharField(label='Search league', max_length=100)
    # country_id = forms.CharField(label='Search country', max_length=100)
    country_name = forms.CharField(label='Search Country name', max_length=100)
    _from = forms.CharField(label='Search _from', max_length=100, required=False)
    to = forms.CharField(label='Search to', max_length=100)

class Bet(forms.Form):
    CHOICES = [('HOME WINS', 'HOME WINS'),
               ('DRAW', 'DRAW'),
               ('AWAY WINS', 'AWAY WINS')]
    bet = forms.ChoiceField(label='Bet on this game:', choices=CHOICES, widget=forms.RadioSelect)

