from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate

from games.models import Game
from django.shortcuts import redirect
from .forms import RegisterBet, DeleteForm

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
                #'form': self.del_form
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
                    messages.success(request, "Bet deleted correctly")
            messages.error(request, "Form is not Valid")
        messages.error(request, "User not logged")
        return redirect('bets')

class Register(TemplateView, View):

    template_name = 'bets.html'
    register_form = RegisterBet

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            messages.error(request, "User not logged")
            return
        form = self.register_form(data=request.POST)
        if not form.is_valid():
            messages.error(request, "Form is not Valid")
            return

        amount = float(form.data['amount'])
        if user.balance < amount:
            messages.error(request, "Not Enough Credit")
            return

        game_id= form.data['game']
        game_bet= form.data['game_bet']

        g = Game()
        game = g.add_game(game_id)
        user.withdraw_credits(amount)
        user.save()
        bet = Bet(user=user, game=game, amount=amount, game_bet=game_bet)
        bet.save()

        messages.success(request, "Bet saved")
        return redirect('bets')
