from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenBlacklistView, TokenRefreshView
from .views import *

urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenRefreshView.as_view()),
    path("users/login/verify/", TokenVerifyView.as_view()),
    path("users/login/killtoken/", TokenBlacklistView.as_view()),
    path("users/", UserView.as_view()),
]