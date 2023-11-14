from rest_framework import serializers
from authentication.models import CustomUser


class APILoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class APIRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()


class APIProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')