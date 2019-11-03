from django.contrib.auth.models import AbstractUser
from django.db import models


class Game(models.Model):
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
    Winner = models.CharField(max_length=100)


