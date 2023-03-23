from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import *

urlpatterns = [
    # Rotas da Documentação
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # Rotas das views
    path("register/", RegisterView.as_view()),
    path("register/resume/", RegisterResume.as_view()),
    path("register/<int:id>/", RegisterDetailsView.as_view()),
]