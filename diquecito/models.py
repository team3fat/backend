# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Usuario(models.Model):

    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(max_length=25, blank=False, null=True)
    password = models.CharField(max_length=20, unique=True, blank=True, null=True, default=None)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.first_name, self.last_name, self.email, self.password)


class Post(models.Model):

    usuario_id = models.ForeignKey(Usuario, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.usuario_id, self.title, self.description)


class Reservation(models.Model):

    comienzo = models.DateField(default=datetime.now, blank=True, null=True)
    final = models.DateField(default=datetime.now, blank=True, null=True)
    
    ESTADO = [
        ('PEDIDO', 'Pedido'),
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO, default='DISPONIBLE')

    def __str__(self):
        return '{}, {}, {}'.format(self.comienzo, self.final, self.estado)


class Qualification(models.Model):

    post_id = models.ForeignKey(Post, default=1, on_delete=models.CASCADE)

    VOTE_CHOICES = (
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
    )
    vote_choices = models.IntegerField(unique=True, blank=True, null=True, default=1, choices=VOTE_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.post_id, self.vote_choices)