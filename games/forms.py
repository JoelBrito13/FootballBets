from django.contrib.auth.forms import UserCreationForm

from users.models import Person
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username',)


class SearchGame(forms.Form):
    query = forms.CharField(label='Search game', max_length=100)
