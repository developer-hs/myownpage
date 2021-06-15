from schedules.models import Schedule
from rest_framework.serializers import ModelSerializer, DateTimeField, CharField


class ScheduleSerializer(ModelSerializer):

    start = DateTimeField(format="%Y-%m-%dT%H:%M", input_formats=None)
    end = DateTimeField(format="%Y-%m-%dT%H:%M", input_formats=None)

    class Meta:
        model = Schedule
        fields = (
            "id",
            "name",
            "start",
            "end",
            "color",
            "timed",
            "detail",
        )
        read_only_field = ("id",)
