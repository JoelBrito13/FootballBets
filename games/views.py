from django.views.generic import TemplateView, View

from bets.forms import RegisterBet
from games.forms import *
from games.models import make_request

class GameView(forms.Form, TemplateView, View):
    search = SearchParam
    bet = RegisterBet
    json_data = {"Brazil": ("19", "68"), "Portugal": ("115", "391"), "England": ("41", "148")}

    def get(self, request, *args, **kwargs):
        self.template_name = 'game_template.html'
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        self.template_name='search_results.html'
        form = self.search(data=request.POST)
        if form.is_valid():
            _from = form.cleaned_data['_from']
            to = form.cleaned_data['to']
            country_id, league_id = self.json_data[form.cleaned_data['country_name']]
            api_get = make_request(
                'https://apiv2.apifootball.com/?action'
                '=get_predictions'
                '&from={}'
                '&to={}'
                '&APIkey=141b8a53928078cd692ab00bbba24a1ec56e82d986c1decba0875b11147949c9'
                '&country_id={}'
                '&league_id={}'.format(_from, to, country_id, league_id))
            param = {
                'games': api_get,
                'form': self.bet
            }
            return self.render_to_response(param)
