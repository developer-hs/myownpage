from users.serializers import UserSerializer
from schedules.models import Schedule
from rest_framework.serializers import ModelSerializer


class ScheduleSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Schedule
        fields = (
            "id",
            "name",
            "start",
            "end",
            "color",
            "timed",
            "user",)
        read_only_field = ("id", "user")
