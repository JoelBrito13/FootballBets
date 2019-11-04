import requests
import datetime
import json
from django.db import models


def make_request(url):
    myResponse = requests.get(url, verify=True)
    if (myResponse.ok):
        return json.loads(myResponse.content)
    return myResponse.raise_for_status()         # Error in request


class Game(models.Model):
    # Constants in Model class
    URL_UPDATE = "https://apiv2.apifootball.com/" \
                 "?action=get_predictions" \
                 "&APIkey=141b8a53928078cd692ab00bbba24a1ec56e82d986c1decba0875b11147949c9"
    match_id = models.IntegerField()
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
            jsonResponse=make_request(url)[0]
            self.match_status=jsonResponse['match_status']
            self.match_hometeam_score=jsonResponse['match_hometeam_score']
            self.match_awayteam_score=jsonResponse['match_awayteam_score']

    def match_finished(self):
        return self.match_date < datetime.date.today()

    def __str__(self):
        return "Match: {} {} - {} {} :{} - {}".format(self.match_id,
                                                      self.match_hometeam_name,
                                                      self.match_hometeam_score,
                                                      self.match_awayteam_name,
                                                      self.match_awayteam_score,
                                                      self.match_date,
                                                      self.league_name)
