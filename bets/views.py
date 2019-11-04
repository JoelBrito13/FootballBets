from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate
from games.models import Game
from .forms import CreateBet

from .models import Bet

class BetView(TemplateView, View):
    template_name = 'bets/bets.html'
    model=Bet

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                obj = Bet.objects.all()
            else:
                obj = Bet.objects.filter(user=request.user)
        param = {
            'rows': obj,
            'form':CreateBet}
        return self.render_to_response(param)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.success(request, "You can now login!")
            return
        form = CreateBet(data=request.POST)
        amount=form.cleaned_data['amount']

        user=request.user
        id=form.cleaned_data['game']
        game = Game.add_game(id)

        Bet(match=game, user=user, amount=amount)

    def put(self,request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Bet.objects.exclude()


