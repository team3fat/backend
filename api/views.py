# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from diquecito.models import Usuario
#Importar siempre que se cree un nuevo modelo con su serializers from .serializers import UsuarioSerializer
#from diquecito.models import Usuario
# Create your views here.

@api_view(['GET'])

def current_user(request):
    serializer=UsuarioSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self request):
    serializer = UsuarioSerializer(request.user)