# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(max_length=25, blank=False, null=True)
    password = models.CharField(max_length=20, unique=True, blank=True, null=True, default=None)





class Post(models.Model):

    post_id = models.AutoField(primary_key=True, unique=True)
    usuario_f = models.ForeignKey(Usuario, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=True)


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True, unique=True)
    duration = models.TimeField()
    cost = models.FloatField(null=True, blank=True)
    PAYMENT_METHOD_CHOICES = (
        ("MP", "Mercado Pago"),
    )
    payment_method_choices = models.CharField(max_length=2, choices=PAYMENT_METHOD_CHOICES)


class Qualification(models.Model):
    quialification_id = models.AutoField(primary_key=True, unique=True)
    post_f = models.ForeignKey(Post, on_delete=models.CASCADE)

    VOTE_CHOICES = (
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"),
    )
    vote_choices = models.IntegerField(unique=True, blank=True, null=True, default=1, choices=VOTE_CHOICES)







