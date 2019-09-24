# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin, messages

from .models import *

from collections import namedtuple

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
            message_bit = "%s reservaciones fueron canceladas" % rows_updated
        self.message_user(request, "%s" % message_bit)

    def aceptar_pedido(self, request, queryset):
    	# Anti solapamiento de reservas
        Range = namedtuple('Range', ['comienzo', 'final'])
        puede = False
        rows_updated = 0

        for reser in queryset:
            r1 = Range(comienzo=reser.comienzo, final=reser.final)
            otras = Reservacion.objects.all().filter(estado='RESERVADO')

            for r in otras:
                r2 = Range(comienzo=r.comienzo, final=r.final)
                latest_start = max(r1.comienzo, r2.comienzo)
                earliest_end = min(r1.final, r2.final)

                delta = (earliest_end - latest_start).days + 1
                overlap = max(0, delta)

                if overlap <= 0:
                    self.puede = True
                    self.rows_updated += 1
                    # Actualizar reserva a RESERVADO
                else:
                    self.message_user(request, "Error: Esa fecha ya esta reservada, no se puede confirmar el pedido"
                    	, messages.ERROR)
                    # NO cambiar el estado

            if self.puede:
                pass
                '''
                rows_updated = queryset.update(estado='RESERVADO')
                if rows_updated == 1:
                    message_bit = "1 pedido de reservacion fue confirmado"
                else:
                    message_bit = "%s pedidos de reservacion fueron confirmados" % rows_updated
                self.message_user(request, "%s" % message_bit)
                '''

        if rows_updated == 1:
            message_bit = "1 pedido de reservacion fue confirmado"
        else:
            message_bit = "%s pedidos de reservacion fueron confirmados" % rows_updated
        self.message_user(request, "%s" % message_bit)

        # Old
        '''
        r1 = Range(comienzo=queryset.value_list('comienzo', flat=True), final=queryset.value_list('final', flat=True))

        otras = Reservacion.objects.values('comienzo', 'final')

        for r in otras:
            r2 = Range(comienzo=r.comienzo, final=r.final)
            latest_start = max(r1.comienzo, r2.comienzo)
            earliest_end = min(r1.final, r2.final)

            delta = (earliest_end - latest_start).days + 1

            overlap = max(0, delta)
            if overlap <= 0:
                rows_updated = queryset.update(estado='RESERVADO')
                if rows_updated == 1:
                    message_bit = "1 pedido de reservacion fue confirmado"
                else:
                    message_bit = "%s pedidos de reservacion fueron confirmados" % rows_updated
                self.message_user(request, "%s" % message_bit)
            else:
                pass
			    # error: solapamiento de reservas
         '''

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