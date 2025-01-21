from django.urls import path
from api.views import UsuarioList, PostList, ReservacionList, QualificationList, Login, TokenAuthentication, SignUp, Calendario
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/login', Login.as_view()),
    path('usuario/tokenauth', TokenAuthentication),
    path('post/', PostList.as_view()),
    path('reservacion/', ReservacionList.as_view()),
    path('qualification/', QualificationList.as_view()),
    path('signup/', SignUp.as_view(), name='signup'),
    path('calendario/', Calendario.as_view(), name='calendario'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
