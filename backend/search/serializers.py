from users.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from .models import SearchHistory


class SearchHistorySerializer(ModelSerializer):

    class Meta:
        model = SearchHistory
        fields = ("id", "search_term")
        read_only_fields = ("id",)
