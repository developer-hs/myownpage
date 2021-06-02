from rest_framework import status
from rest_framework.response import Response
from schedules.serializers import ScheduleSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Schedule


class ScheduleAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        user = request.user
        schedule = Schedule.objects.filter(user=user)
        if schedule is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif schedule is not None:
            serializer = ScheduleSerializer(schedule, many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


