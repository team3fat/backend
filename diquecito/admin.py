# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render


# Modelos de Admins

class ReservacionAdmin(admin.ModelAdmin):
	# Orden de listado de datos
    list_display = ('creacion','comienzo','final','estado')

    # Filtro
    list_filter = ('comienzo','final','estado')

    # FieldSets
    fieldsets = (
        (None, {'fields': ('comienzo', 'final','estado')}),
    )

    # Permisos de admin
    def has_delete_permission(self, request, obj=None):
        return False

    # Acciones de admin
    actions = ['cancelar_pedido','aceptar_pedido','resetear_pedido']

    def resetear_pedido(self, request, queryset):
        rows_updated = queryset.update(estado='PEDIDO')
        if rows_updated == 1:
            message_bit = "1 pedido de reservacion fue reseteado"
        else:
            message_bit = "%s pedidos de reservaciones fueron reseteados" % rows_updated
        self.message_user(request, "%s" % message_bit)

    def cancelar_pedido(self, request, queryset):
        rows_updated = queryset.update(estado='CANCELADO')
        if rows_updated == 1:
            message_bit = "1 reservacion fue cancelada"
            
        else:
            send_mail('Pedido de reservacion Rechazado',
            'Lamentamos informarle que su pedido de Reservacion del complejo Diquecito a sido rechazado para saber mas contactenos a este número 351 330-2070',
            'diquecito.a@gmail.com',
            ['yarerih689@mailnet.top'],
            fail_silently=False)
            message_bit = "%s reservaciones fueron canceladas" % rows_updated
        self.message_user(request, "%s" % message_bit)

        

    def aceptar_pedido(self, request, queryset):
        rows_updated = queryset.update(estado='RESERVADO')
        if rows_updated == 1:
            message_bit = "1 pedido de reservacion fue confirmado"
            send_mail('Pedido de reservacion aceptado',
            'Su pedido de reservacion a sido aceptado, en los proximos dias lo contactaremos para acordar el precio, si tiene alguna pregunta puede comuncarse por whatsapp o facebook, Muchas Gracias',
            'diquecito.a@gmail.com',
            ['yarerih689@mailnet.top'],
            fail_silently=False) 

        else:
            send_mail('Pedido de reservacion aceptado',
            'Su pedido de reservacion a sido aceptado, en los proximos dias lo contactaremos para acordar el precio, si tiene alguna pregunta puede comuncarse por whatsapp o facebook, Muchas Gracias',
            'diquecito.a@gmail.com',
            ['yarerih689@mailnet.top'],
            fail_silently=False) 
            message_bit = "%s pedidos de reservacion fueron confirmados" % rows_updated
             
        self.message_user(request, "%s" % message_bit)
        
    # Permisos de acciones
    cancelar_pedido.allowed_permissions = ('change',)
    aceptar_pedido.allowed_permissions = ('change',)
    resetear_pedido.allowed_permissions = ('change',)

    # Nombre de las accciones
    cancelar_pedido.short_description = "Cancelar los pedidos seleccionados"
    aceptar_pedido.short_description = "Aceptar los pedidos seleccionados"
    resetear_pedido.short_description = "Resetear los pedidos seleccionados"


# A implementar a futuro
'''
class ReservationAdmin(admin.ModelAdmin):
	# Orden de listado de datos
	list_display = ('comienzo','final','estado')

	# FieldSets
	fieldsets = (
		(None, {'fields': ('comienzo', 'final','estado')}),
	)
'''

# Admin sites

class ComplejoAdminSite(admin.AdminSite):
	# Textos de la pagina
    site_header = "Admin Complejo Diquecito"
    site_title = "Portal de Admin Complejo Diquecito"
    index_title = "Bienvenido al Portal de Admin Complejo Diquecito"

complejo_admin_site = ComplejoAdminSite(name='complejo_admin')

# Register your models here.

## Admin Site
admin.site.register(Usuario)
admin.site.register(Reservacion)
admin.site.register(Post)
admin.site.register(Qualification)

## Complejo Admin Site
complejo_admin_site.register(ReservacionProxy, ReservacionAdmin)
# A implementar a futuro
'''
complejo_admin_site.register(UsuarioProxy, UsuarioAdmin)
'''

# Dehabilitacion de la accion "Eliminar seleccionados"
complejo_admin_site.disable_action('delete_selected')