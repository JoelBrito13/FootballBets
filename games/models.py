import requests
import datetime
import json
from django.db import models


def make_request(url):
    myResponse = requests.get(url, verify=True)
    if (myResponse.ok):
        return json.loads(myResponse.content)
    return myResponse.raise_for_status()  # Error in request


class Game(models.Model):
    # Constants in Model class
    URL_UPDATE = "https://apiv2.apifootball.com/" \
                 "?action=get_predictions" \
                 "&APIkey=141b8a53928078cd692ab00bbba24a1ec56e82d986c1decba0875b11147949c9"
    match_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=50)
    league_name = models.CharField(max_length=70)
    match_date = models.DateField()
    match_status = models.CharField(max_length=50)
    match_time = models.TimeField()
    match_hometeam_name = models.CharField(max_length=70)
    match_hometeam_score = models.IntegerField()
    match_awayteam_name = models.CharField(max_length=70)
    match_awayteam_score = models.IntegerField()
    prob_HW = models.FloatField()
    prob_D = models.FloatField()
    prob_AW = models.FloatField()

    def update(self):
        if self.match_finished():
            url = "{}&match_id={}".format(self.URL_UPDATE, self.match_id)
            jsonResponse = make_request(url)[0]
            self.match_status = jsonResponse['match_status']
            self.match_hometeam_score = jsonResponse['match_hometeam_score']
            self.match_awayteam_score = jsonResponse['match_awayteam_score']

    def match_finished(self):
        return self.match_date < datetime.date.today()

    def add_game(self, search_id):
        if not Game.objects.exists(search_id):
            url = "{}&match_id={}".format(self.URL_UPDATE, search_id)
            jsonResponse = make_request(url)[0]

            self.match_id = jsonResponse['match_id']
            self.country_name = jsonResponse['country_name']
            self.league_name = jsonResponse['league_name']
            self.match_date = jsonResponse['match_date']
            self.match_status = jsonResponse['match_status']
            self.match_time = jsonResponse['match_time']
            self.match_hometeam_name = jsonResponse['match_hometeam_name']
            self.match_hometeam_score = jsonResponse['match_hometeam_score']
            self.match_awayteam_name = jsonResponse['match_awayteam_name']
            self.match_awayteam_score = jsonResponse['match_awayteam_score']
            self.prob_HW = jsonResponse['prob_HW']
            self.prob_D = jsonResponse['prob_D']
            self.prob_AW = jsonResponse['prob_AW']
            return self

        return Game.objects.get(search_id)

    def __str__(self):
        return "{} match: {}, {} x {} - {}".format(self.league_name,
                                                   self.match_id,
                                                   self.match_hometeam_name,
                                                   self.match_awayteam_name,
                                                   self.match_date)
