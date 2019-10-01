from django.urls import path
from api.views import UsuarioList, PostList, ReservacionList, QualificationList, Login, TokenAuthentication, SignUp, Calendario
from . import views

urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/login', Login),
    path('usuario/tokenauth', TokenAuthentication),
    path('post/', PostList.as_view()),
    path('reservacion/', ReservacionList.as_view()),
    path('qualification/', QualificationList.as_view()),
    path('signup/', SignUp.as_view(), name='signup'),
    path('calendario/', Calendario.as_view(), name='calendario'),
    path('mail/', views.ReservacionList.mail),
]
