from rest_framework import status
from bets.serializers import GameSerializer, BetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Bet, Game


class BetView(APIView):
    def get(self, request):
        bets = Bet.objects.all()
        serializer = BetSerializer(bets, many=True)
        [bet.update_status() for bet in bets]
        return Response(serializer.data)

    def post(self, request):
        serializer = BetSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = int(request.GET['bet'])
        try:
            bet = Bet.objects.get(id=id)
        except Bet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Bet.delete(bet)
        return Response(BetSerializer(data=bet).data)


@api_view(['GET'])
def view_game(request, match_id):
    try:
        game = Game.objects.filter(match_id=match_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)
