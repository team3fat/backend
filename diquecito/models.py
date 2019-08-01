# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

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

    duration = models.TimeField()
    cost = models.FloatField(null=True, blank=True)
    PAYMENT_METHOD_CHOICES = (
        ("MP", "Mercado Pago"),
    )
    payment_method_choices = models.CharField(max_length=2, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return '{}, {}, {}'.format(self.duration, self.cost, self.payment_method_choices)


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