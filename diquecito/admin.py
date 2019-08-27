# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

@admin.register(Reservation,Usuario)
class ComplejoAdmin(admin.ModelAdmin):
    pass

# Register your models here.

admin.site.register(Reservation)
admin.site.register(Post)
admin.site.register(Qualification)
admin.site.register(Usuario)
