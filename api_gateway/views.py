from django.http import JsonResponse
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import APILoginSerializer, APIRegistrationSerializer
import requests
import logging
import os

# Настройка логгера
logger = logging.getLogger(__name__)


class APIRegistrationView(APIView):
    def post(self, request):
        serializer = APIRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                registration_url = os.environ.get("REGISTRATION_SERVICE_URL",
                                                  "http://registration-service/api/register/")
                response = requests.post(registration_url, data=request.data, timeout=5)

                if response.status_code == 201:
                    return Response(response.json(), status=status.HTTP_201_CREATED)
                else:
                    logger.error(f"Registration failed with status {response.status_code}")
                    return Response({'error': 'Registration failed'}, status=response.status_code)

            except requests.exceptions.RequestException as e:
                logger.error(f"Error during registration request: {e}")
                return Response({'error': 'Registration service unavailable'},
                                status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APILoginView(APIView):
    def post(self, request):
        serializer = APILoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                login_url = os.environ.get("LOGIN_SERVICE_URL", "http://authentication-service/api/login/")
                response = requests.post(login_url, data=request.data, timeout=5)

                if response.status_code == 200:
                    return Response(response.json(), status=status.HTTP_200_OK)
                else:
                    logger.error(f"Login failed with status {response.status_code}")
                    return Response({'error': 'Login failed'}, status=response.status_code)

            except requests.exceptions.RequestException as e:
                logger.error(f"Error during login request: {e}")
                return Response({'error': 'Login service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if not token:
            return JsonResponse({'error': 'Token is missing'}, status=401)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.DecodeError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        request.user_payload = payload