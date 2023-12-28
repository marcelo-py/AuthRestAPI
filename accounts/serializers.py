from rest_framework import serializers
from .models import UserAuth


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()