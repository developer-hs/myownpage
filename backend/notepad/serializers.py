from rest_framework.serializers import ModelSerializer, BooleanField
from users.serializers import UserSerializer
from .views import NotePads


class NotePadSerializer(ModelSerializer):
    done = BooleanField(read_only=True)

    class Meta:
        model = NotePads
        fields = ("id", "memo", "done", "datetime_created", "datetime_update")
        read_only_fields = ("id", "datetime_created", "datetime_update")
