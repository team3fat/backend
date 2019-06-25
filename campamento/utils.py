from api.serializers import UsuarioSerializer

# custom JWT response payload handler which includes the user’s serialized data
def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UsuarioSerializer(user, context={'request': request}).data
}