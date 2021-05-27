from rest_framework.response import Response
import notepad
from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import NotePads
from .serializers import NotePadSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def user_notepads(request):
    memos = NotePads.objects.filter(user=request.user)
    serializer = NotePadSerializer(memos , many=True)
    return Response(serializer.data)