import jwt, json
from rest_framework import serializers, views
from rest_framework.response import Response
from diquecito.models import Usuario, Post, Reservation, Qualification

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
        fields = ('duration', 'cost', 'payment_method_choices')

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('post_id', 'vote_choices')

'''
class UsuarioSerializer(serializers.Serializer):
    usuario_id = serializers.AutoField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Usuario` instance, given the validated data.
        """
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
'''

# Sin usar el handler
class Login(views.APIView):
    def post(selfself, request, *args, **kwargs):
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
