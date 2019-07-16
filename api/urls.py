from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/login', Login),
    path('usuario/tokenauth', TokenAuthentication),
    path('post/', PostList.as_view()),
    path('reservation/', ReservationList.as_view()),
    path('qualification/', QualificationList.as_view()),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
