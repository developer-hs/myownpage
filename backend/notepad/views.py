from decimal import ConversionSyntax
from django.core.exceptions import RequestDataTooBig
from rest_framework import status
from rest_framework.response import Response
import notepad
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import NotePads
from .serializers import NotePadSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def user_notepads_info(request):
    memos = NotePads.objects.filter(user=request.user)
    serializer = NotePadSerializer(memos, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def create_memo(request):
    memo = NotePads.objects.filter(memo=request.data.get("memo") , user = request.user)
    if not memo:
        serializer = NotePadSerializer(
            data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def remove_memo(request):
    request_memo = request.data.get("memo")
    user = request.user
    memo = NotePads.objects.get(memo=request_memo , user=user)
    print(memo)
    memo.delete()
    return Response(status=status.HTTP_200_OK)
