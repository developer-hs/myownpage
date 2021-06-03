from schedules.models import Schedule
from rest_framework.serializers import ModelSerializer, DateTimeField



class ScheduleSerializer(ModelSerializer):

    start = DateTimeField(format="%Y-%m-%d %H:%M", input_formats=None)
    end = DateTimeField(format="%Y-%m-%d %H:%M", input_formats=None)

    class Meta:
        model = Schedule
        fields = (
            "id",
            "name",
            "start",
            "end",
            "color",
            "timed",
            )
        read_only_field = ("id",)
