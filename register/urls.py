from django.urls import path

from .views import *

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("register/resume/", RegisterResume.as_view()),
    path("register/<id>/", RegisterDetailsView.as_view()),
]