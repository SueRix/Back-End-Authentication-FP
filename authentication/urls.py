from django.urls import path
from .views import UserRegistrationView
from .views import CustomLoginView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
