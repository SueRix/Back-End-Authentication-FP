from django.urls import path, include
from .views import APIRegistrationView, APILoginView

urlpatterns = [
    path('registration/', APIRegistrationView.as_view(), name='registration-gateway'),
    path('login/', APILoginView.as_view(), name='login-gateway'),
]