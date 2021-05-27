from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from .views import NotePads

class NotePadSerializer(ModelSerializer):

    class Meta:
        model = NotePads
        fields = ("memo","datetime_created","datetime_update")