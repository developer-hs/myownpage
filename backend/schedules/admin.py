from django.contrib import admin
from . import models
@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display=("user","name")