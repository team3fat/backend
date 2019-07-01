from diquecito.models import Usuario, Post, Reservation, Qualification
from diquecito.serializers import UsuarioSerializer, PostSerializer, ReservationSerializer, QualificationSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class QualificationList(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
