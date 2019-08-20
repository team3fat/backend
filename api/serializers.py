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
    dias = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        #TODO ¿fields????

    def get_dias(self, obj):
        # TODO logica que toma lista de objetos "reservation" del modelo y retorna
        """" [
            
        {
            "fecha": "13/12/2019",
            "estado": "disponible"
        },
        {
            "fecha": "14/12/2019",
            "estado": "reservado"
        }
    ]"""
    """
            start_date = datetime.date(2005, 1, 1)
            end_date = datetime.date(2005, 3, 31)
            Entry.objects.filter(pub_date__range=(start_date, end_date))
    """
        # def crearDias(self):
        #     calendario = {'dias': []}
        #     # calendario_json = json.dumps(calendario)
        #     """for i in list(range(2)):
        #         dia = json.dumps({'fecha':"01/02/2019", 'estado':"RESERVADO"})
        #         calendario.dias.append(dia)"""

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

