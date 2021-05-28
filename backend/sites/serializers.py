from rest_framework import serializers
from .models import BookmarkSites, InputSite


class InputSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSite
        fields = ["name", ]
        read_only_field = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    sites = InputSiteSerializer(read_only=True, many=True)

    class Meta:
        model = BookmarkSites
        fields = ["id", "sites", "locked"]
        read_only_fields = ("id")
