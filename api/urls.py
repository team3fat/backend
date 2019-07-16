from django.urls import path
from .views import *

urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/login', Login),
    path('usuario/tokenauth', TokenAuthentication),
    path('post/', PostList.as_view()),
    path('reservation/', ReservationList.as_view()),
    path('qualification/', QualificationList.as_view()),
]
