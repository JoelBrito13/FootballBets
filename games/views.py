import json

from django.forms import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, ListView
from django.db.models import Q

# from games.forms import SearchGame
from games.forms import *
from games.models import Game, make_request
from datetime import date


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
    template_name = 'search_results.html'
    search = SearchParam
    bet = Bet
    json_data = {"Brazil": ("19", "68"), "Portugal": ("115", "391"), "England": ("41", "148")}

    def get(self, request, *args, **kwargs):
        print("ENTRA")
        bet = self.bet()
        form = SearchParam()

        return self.render_to_response({'form': form, 'bet' : bet})

    def post(self, request, *args, **kwargs):
        form = self.search(data=request.POST)
        bet = self.bet()
        # if not form.cleaned_data['_from']:
        #     _from = str(date.today())
        # else:
        #     if form.is_valid():
        #         _from = form.cleaned_data['_from']
        if form.is_valid():
            # league_id = form.cleaned_data['league_id']
            # country_id = form.cleaned_data['country_name']
            _from = form.cleaned_data['_from']
            # if not _from:
            #     _from = date.today()
            # else:
            #     _from = form.cleaned_data['_from']
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
            search = {
                'games': api_get,
                'bet'  : bet
            }
            return self.render_to_response(search)
