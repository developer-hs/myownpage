from rest_framework import status, generics, mixins
from rest_framework.response import Response
from schedules.serializers import ScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Schedule
from datetime import datetime


class ScheduleAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def schedule_obj_init(self):
        date_obj = self.date_obj_init()
        schedule_obj = dict(self.request.data, **date_obj)
        return schedule_obj

    def date_obj_init(self):
        dates = self.request.data.get("dates")
        time = self.request.data.get("time")
        timed = self.request.data.get("timed")
        schedule_obj = {}
        self.date_conversion(time, dates, timed, schedule_obj)
        return schedule_obj

    def date_conversion(self, time: str, dates: list, timed: bool, schedule_obj: dict):
        first_check = True

        hours, minute = 0, 0
        if timed:
            hours, minute = time.split(":")
        for date in dates:
            year, month, day = date.split("-")
            year, month, day, hours, minute = \
                int(year), int(month), int(day), int(hours), int(minute)
            if first_check:
                schedule_obj["start"] = datetime(
                    year, month, day, hours, minute)
                first_check = False
            else:
                schedule_obj["end"] = datetime(
                    year, month, day, 0, 0)
        return schedule_obj

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        schedule_obj = self.schedule_obj_init()
        serializer = ScheduleSerializer(data=schedule_obj)
        if serializer.is_valid():
            new_schedule = serializer.save(user=request.user)
            new_schedule_serializer = ScheduleSerializer(new_schedule).data
            return Response(new_schedule_serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        if schedule is not None:
            if schedule.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            schedule.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule_obj = self.schedule_obj_init()
        if schedule is not None:
            if schedule.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = ScheduleSerializer(
                schedule, schedule_obj, partial=True)
            if serializer.is_valid():
                schedule = serializer.save()
                schedule_serializer = ScheduleSerializer(schedule).data
                return Response(schedule_serializer, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
