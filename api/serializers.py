from rest_framework import serializers

from diquecito.models import Usuario, Post, Reservacion, Qualification

import json

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'password')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('usuario_id', 'title', 'description')

class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = ('comienzo', 'final', 'estado')

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = ('comienzo', 'final', 'estado')

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('post_id', 'vote_choices')    

