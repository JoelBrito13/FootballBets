from rest_framework.decorators import api_view
from users.serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import Person

@api_view(['GET'])
def get_users(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


