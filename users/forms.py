from django.contrib.auth.forms import UserCreationForm

from users.models import Person
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'balance')


class LoadCreditsForm(forms.Form):
    insert_credit = forms.FloatField(required=False, min_value=1)
    withdraw_credit = forms.FloatField(required=False, min_value=1)
