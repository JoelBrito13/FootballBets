from django.contrib.auth.forms import UserCreationForm

from users.models import Person
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'balance')


class LoadCreditsForm(forms.Form):
    insert_credit = forms.CharField(max_length=100, label=' Insert Credits', required=False)
    withdraw_credit = forms.CharField(max_length=100, label='Withdraw Credits', required=False)
