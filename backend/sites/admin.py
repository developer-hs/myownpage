from django.contrib import admin
from . import models

@admin.register(models.InputSite)
class InputSiteAdmin(admin.ModelAdmin):
    list_display = ("site_url",)
    
@admin.register(models.BookmarkSites)
class SiteAdmin(admin.ModelAdmin):

    filter_horizontal = ("sites",)
