from django import forms

class CreateBet(forms.Form):
    user = forms.IntegerField
    game = forms.IntegerField
    amount = forms.FloatField

class DeleteForm(forms.Form):
    bet_id_del = forms.IntegerField(label='Bets')


class RegisterBet(forms.Form):
    GAME_RESULTS = (
        ('HW', 'Home Win'),
        ('D', 'Draw'),
        ('AW', 'Away Win')
    )

    game = forms.IntegerField
    amount = forms.FloatField
    game_bet = forms.CheckboxInput

                                         #game_bet = forms.MultipleChoiceField(choices=GAME_RESULTS,
                                   #      widget=forms.CheckboxSelectMultiple
                                    #     )


