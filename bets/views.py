from rest_framework import status
from bets.serializers import GameSerializer, BetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Token
from rest_framework.views import APIView

from .models import Bet, Game


class BetView(APIView):
    def get(self, request):
        user = get_user(request)
        if user.is_authenticated:
            if user.is_superuser:
                bets = Bet.objects.all()
            else:
                bets = Bet.objects.filter(user=user)

            serializer = BetSerializer(bets, many=True)
            [bet.update_status() for bet in bets]
            return Response(serializer.data)

    def post(self, request):
        user = get_user(request)
        if not user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = BetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            game_check = serializer.validated_data['game']
            if game_check.match_status == 'Finished':
                return Response({"ERROR":"Cannot create bet of a finished game"}, status=status.HTTP_400_BAD_REQUEST)
            if user.is_superuser:
                serializer.save()
            elif user == serializer.validated_data['user'] :
                amount = serializer.validated_data['amount']
                if user.balance < amount:
                    return Response({"ERROR": "Amount not enough"}, status=status.HTTP_400_BAD_REQUEST)
                user.withdraw_credits(amount)
                serializer.save()
            else:
                return Response({"ERROR": "User not Valid"}, status=status.HTTP_401_UNAUTHORIZED)
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


def get_user(request):
    token = request.headers['Authorization'].split(" ")[1]
    return Token.objects.get(key=token).user
