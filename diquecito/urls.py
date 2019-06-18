from django.urls import path
from diquecito.views import *

urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('post/', PostList.as_view()),
    path('reservation/', ReservationList.as_view()),
    path('qualification/', QualificationList.as_view())
]
