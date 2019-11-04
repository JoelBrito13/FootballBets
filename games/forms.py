from django import forms


class SearchGame(forms.Form):
    query = forms.CharField(label='Search game', max_length=100)
