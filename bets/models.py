from django.db import models
from users.models import Person
from games.models import Game

class Bet(models.Model):
    # Constants in Model class
    HOME_WIN = 'HW'
    DRAW = 'D'
    AWAY_WIN = 'AW'
    GAME_RESULTS = (
        (HOME_WIN, 'Home Win'),
        (DRAW, 'Draw'),
        (AWAY_WIN, 'Away Win')
    )
    game = models.ForeignKey(Game)
    user = models.ForeignKey(Person)
    game_bet = models.CharField(
        max_length=2,
        choices=GAME_RESULTS
    )
    amount = models.FloatField
    game_finished = models.BooleanField(
        default=False
    )
    balance = models.FloatField(
        default=0
    )

    def updateStatus(self):
        if self.game_finished:
            return
        if Game.match_status == 'Finished':
            self.user.insert_credits(
                self.update_balance()
            )

            self.game_finished = True

    def update_balance(self):
        if self.game_bet == self.define_result():
            return self.amount * 100 / self.get_prob()
        return 0

    def define_result(self):
        home = self.game.match_hometeam_score
        away = self.game.match_awayteam_score
        if home > away:
            return self.HOME_WIN
        elif home < away:
            return self.AWAY_WIN
        else:
            return self.DRAW

    def get_prob(self):
        if self.game_bet == self.HOME_WIN:
            return self.game.prob_HW
        if self.game_bet == self.AWAY_WIN:
            return self.game.prob_AW
        if self.game_bet == self.DRAW:
            return self.game.prob_D

    def __str__(self):
        return "Bet Info(<{} {} {}>)".format(self.game, self.game_bet, self.amount)
