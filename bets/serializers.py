from bets.models import Bet, Game
from rest_framework import serializers


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            'id',
            'game',
            'user',
            'game_bet',
            'amount',
            'game_finished',
            'balance'
        )

    def __init__(self, instance=None, data=None,  **kwargs):
        if "data" in kwargs:
            data = kwargs.pop("data")
            if "game" in data:
                search_id = data.pop("game")
                game = Game()
                game.add_game(search_id)
        super(BetSerializer, self).__init__(instance=instance, data=data, **kwargs)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'match_id',
            'country_name',
            'league_name',
            'match_date',
            'match_status',
            'match_time',
            'match_hometeam_name',
            'match_hometeam_score',
            'match_awayteam_name',
            'match_awayteam_score',
            'prob_HW',
            'prob_D',
            'prob_AW'
        )

    def __init__(self, instance=None, data=None, **kwargs):
        super(GameSerializer, self).__init__(instance=instance, data=data, **kwargs)
