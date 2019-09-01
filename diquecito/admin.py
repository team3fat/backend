# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Admin de reservacion y usuarios
""" 
@admin.register(Reservation,Usuario)
class ComplejoAdmin(admin.ModelAdmin):
    pass
 """

# Modelos de Admins

class ReservationAdmin(admin.ModelAdmin):
	# Orden de listado de datos
    list_display = ('creacion','comienzo','final','estado')

    # FieldSets
    fieldsets = (
        (None, {'fields': ('comienzo', 'final','estado')}),
    )

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
admin.site.register(Reservation)
admin.site.register(Post)
admin.site.register(Qualification)

## Complejo Admin Site
complejo_admin_site.register(ReservationProxy, ReservationAdmin)
# A implementar a futuro
'''
complejo_admin_site.register(UsuarioProxy, UsuarioAdmin)
'''