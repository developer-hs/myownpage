from django.contrib import admin
from . import models


@admin.register(models.SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ("search_term", "user")
