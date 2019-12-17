from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from users.serializers import PersonSerializer, AddPersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import parsers, renderers, status

from users.models import Person, Token

from rest_framework.views import APIView


@api_view(['GET'])
def get_users(request):
    user = get_user(request)
    if user.is_authenticated:

        if user.is_superuser:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data)

        serializer = PersonSerializer(user)
        return Response(serializer.data)
    return Response({'ERROR': 'User not Valid'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_user(request):
    serializer = AddPersonSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"ERROR": "Error trying to create user"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class Balance(APIView):
    def get(self, request, amount = 0):
        user = get_user(request)
        if user.is_authenticated:
            if amount != 0:
                user.balance += int(amount)
                user.save()
            return Response({'amount': user.balance})

        return Response({'ERROR': 'User not Valid'}, status=status.HTTP_401_UNAUTHORIZED)


obtain_auth_token = ObtainAuthToken.as_view()


def get_user(request):
    token = request.headers['Authorization'].split(" ")[1]
    return Token.objects.get(key=token).user
