from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings

from rest_framework.response import Response
from rest_framework import status
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(
        write_only=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        # fields = ('username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            user.save()

            print(user, "<<<<<<USER NIH")
            return user
            # return Response(user, status=status.HTTP_201_CREATED)

        except Exception as error:
            return Response({
                "detail": str(error)
            },
                status=status.HTTP_400_BAD_REQUEST,
            )