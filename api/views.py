# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt, json
from django.http import HttpResponse
from rest_framework import views, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import generics as rest_generics
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic as generics
from diquecito.models import Usuario, Post, Reservacion, Qualification
from .serializers import UsuarioSerializer, PostSerializer, ReservacionSerializer, QualificationSerializer, CalendarioSerializer
from django_filters import rest_framework as filters
from django.utils import timezone
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters.rest_framework
from django.core.mail import send_mail

# Create your views here.

@api_view(['GET'])

def current_user(request):
    serializer = UsuarioSerializer(request.user)
    return Response(serializer.data)

class UsuarioList(rest_generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class PostList(rest_generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj




    
class ReservacionList(rest_generics.ListCreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer


    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

    def mail(request):
        send_mail(
        'Pedido de reservacion',
        'Un usuario a realizado un pedido de reserva desde el dia {comienzo} hasta {final}.',
        'diquecito.a@gmail.com',
        ['tomy.monier@gmail.com'],
        fail_silently=False,
    )

# View que devolvera la lista de reservaciones

class Calendario(rest_generics.ListCreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = CalendarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$comienzo', '$final']

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class QualificationList(rest_generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

# Sin usar el handler
class Login(views.APIView):
    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Falta de nombre de usuario y/o contraseña"}, status="400")

        username = request.data['username']
        password = request.data['password']

        try:
            user = Usuario.objects.get(username=username, password=password)
        except Usuario.DoesNotExist:
            return Response({'Error': "Nombre de usuario y/o contraseña invalido/s"}, status="400")

        if user:
            payload = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
                json.dumps(jwt_token),
                status=200,
                content_type="application/json"
            )
        else:
            return Response(
                json.dumps({'Error': "Credenciales invalidas"}),
                status=400,
                content_type="application/json"
            )

class TokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return Usuario

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None
        if len(auth) == 1:
            msg = 'Token invalido. Credenciales invalidas'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Token invalido'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Token invalido (Es null)'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Token invalido. El token no deberia tener caracteres invalidos'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        self.model = self.get_model()
        payload = jwt.decode(token, "SECRET_KEY")
        email = payload['email']
        userid = payload['id']
        msg = {'Error': "Token erroneo", 'status': "401"}
        try:
            user = Usuario.objects.get(
                email=email,
                id=userid,
                is_active=True
            )

            if not user.token['token'] == token:
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token invalid"}, status="403")
        except Usuario.DoesNotExist:
            return HttpResponse({'Error': "Error interno del servidor"})

        return(user, token)

    def authenticate_header(self, request):
        return 'Token'

class SignUp(generics.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

