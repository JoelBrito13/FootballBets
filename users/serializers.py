from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from users.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'description',
            'is_superuser',
            'balance',
            'username',
            'first_name',
            'last_name',
            'email',
            'balance'
        )

class AddPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'description',
        )



class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
