from decimal import ConversionSyntax
from django.db import connections
from django.db.models.query import FlatValuesListIterable
from rest_framework import status
from rest_framework.response import Response
from schedules.serializers import ScheduleSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Schedule
from datetime import datetime, time


class ScheduleAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def schedule_obj_init(self):
        name = self.request.data.get("name")
        color = self.request.data.get("color")
        timed = self.request.data.get("timed")
        dates = self.request.data.get("dates")
        time = self.request.data.get("time")
        detail = self.request.data.get("detail")
        schedule_obj = {"name": name, "color": color,
                        "timed": timed, "detail": detail}
        self.date_conversion(time, dates, schedule_obj)
        return schedule_obj

    def date_conversion(self, time: str, dates: list, schedule_obj: dict):
        first_check = True

        hours, minute = 0, 0
        if schedule_obj["timed"]:
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

    def get(self, request):
        user = request.user
        schedule = Schedule.objects.filter(user=user)
        if schedule is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif schedule is not None:
            serializer = ScheduleSerializer(schedule, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        schedule_obj = self.schedule_obj_init()
        serializer = ScheduleSerializer(data=schedule_obj)
        print(serializer)
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
