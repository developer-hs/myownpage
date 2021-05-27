from django.contrib import admin
from . import models

@admin.register(models.NotePads)
class NotePadAdmin(admin.ModelAdmin):
    list_display = ("memo" , "user")