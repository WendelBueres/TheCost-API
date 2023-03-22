from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserView

urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/", UserView.as_view()),
]