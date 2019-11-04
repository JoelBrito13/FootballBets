from django import forms


class SearchGame(forms.Form):
    search = forms.CharField(label='Search game', max_length=100)
