from rest_framework import serializers

from diquecito.models import Usuario, Post, Reservation, Qualification

import json

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'password')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('usuario_id', 'title', 'description')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('comienzo', 'final', 'estado')

"""
class CalendarioSerializer(serializers.Serializer):
    def crearDias():
        calendario = {'dias':[]}
        calendario_json = json.dumps(calendario)
        for i in list(range(2)):
            dia = json.dumps({'fecha':"01/02/2019", 'estado':"RESERVADO"})
            calendario.dias.append(dia)

        return calendario

    dias = crearDias()
"""

class CalendarioSerializer(serializers.Serializer):
    fecha = serializers.DateTimeField()
    estado = serializers.CharField(max_length=20)

# Uso:
# Serializacion:
# from rest_framework.renderers import JSONRenderer
# serializer = CalendarioSerializer(calendario)
# json = JSONRenderer().render(serializer.data)
# Deserializacion:
# import io
# from rest_framework.parsers import JSONParser
# stream = io.BytesIO(json)
# data = JSONParser().parse(stream)
# serializer = CommentSerializer(data=data)

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('post_id', 'vote_choices')    

