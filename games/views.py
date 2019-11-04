from django.forms import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, ListView
from django.db.models import Q

from games.forms import SearchGame
from games.models import Game, make_request
import datetime


class GameView(forms.Form, TemplateView, View):
    template_name = 'game_template.html'

    def get(self, request, *args, **kwargs):
        api_get = make_request(
            'https://apiv2.apifootball.com/?action=get_predictions&from=2019-11-0&to=2019-12-0&APIkey=141b8a53928078cd692ab00bbba24a1ec56e82d986c1decba0875b11147949c9&country_id=19&league_id=68')
        query = {
            'games': api_get
        }
        return self.render_to_response(query)


class SearchView(forms.Form, TemplateView, View):
    search = SearchGame
    template_name = 'search_results.html'

    def post(self, request, *args, **kwargs):
        form = self.search(data=request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            games = Game.objects.filter(match_hometeam_name__icontains=query)
            return self.render_to_response({'games': games, 'query': query})
        return self.render_to_response({'form': form})

    def get(self, request, *args, **kwargs):
        form = SearchGame()
        return self.render_to_response({'form': form})
