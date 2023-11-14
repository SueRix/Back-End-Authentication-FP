from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import CustomUser
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")
        return value

    def validate_password(self, value):
        password = value
        confirm_password = self.initial_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match!")

        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long!")

        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # def validate(self, data):
    #     user = authenticate(username=data['username'], password=data['password'])
    #     if not user:
    #         raise serializers.ValidationError("Invalid credentials")
    #     return data
