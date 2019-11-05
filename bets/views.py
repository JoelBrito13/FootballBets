from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate

from games.models import Game
from django.shortcuts import redirect
from .forms import CreateBet, DeleteForm

from .models import Bet

class BetView(TemplateView, View):
    template_name = 'bets/bets.html'
    model = Bet
    del_form=DeleteForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                obj = Bet.objects.all()
            else:
                obj = Bet.objects.filter(user=request.user)
            [x.update_status() for x in obj]
            param = {
                'rows': obj,
                'form': CreateBet,
                'deleteForm': self.del_form
            }
            return self.render_to_response(param)

        messages.error(request, "You must be logged!")
        return redirect('home')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.del_form(data=request.POST)
            if form.is_valid():
                bet_id_del = form.cleaned_data['bet_id_del']
                bet = Bet.objects.get(bet_id_del)
                if bet.user == request.user or request.user.is_superuser:
                    bet.user.insert_credits(bet.amount)  # return credit to user
                    bet.delete()
                    messages.success("Bet deleted correctly")
            messages.error("Form is not Valid")
        messages.error("User not logged")
        return redirect('bets')

class Alter(TemplateView, View):
    template_name = 'bets/modify_bet.html'
    model = Bet

    def get(self, request, *args, **kwargs):
        bet = kwargs['bet']
        if request.user.is_authenticated:
            if request.user.is_superuser:
                obj = Bet.objects.get(bet)
            else:
                obj = Bet.objects.filter(user=request.user, id=bet)
            param = {
                'rows': obj
            }
        messages.success(request, "You must be logged!")
        return redirect('home')


class Test(TemplateView, View):
    template_name = 'bets/test.html'
    model = Bet

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                obj = self.model.objects.all()
            else:
                obj = self.model.objects.filter(user=request.user)
        param = {
            'rows': obj,
            'form': CreateBet}
        return self.render_to_response(param)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, "You can now login!")
            return
        form = CreateBet(data=request.POST)
        amount = form.cleaned_data['amount']

        user = request.user
        id = form.cleaned_data['game']
        game = Game.add_game(id)

        Bet(match=game, user=user, amount=amount)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Bet.objects.exclude()
