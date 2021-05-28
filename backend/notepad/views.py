from decimal import ConversionSyntax
from django.contrib.auth import authenticate
from django.core.exceptions import RequestDataTooBig
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import notepad
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import NotePads
from .serializers import NotePadSerializer



class NotepadsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def get(self,request):
        memos = NotePads.objects.filter(user=request.user)
        serializer = NotePadSerializer(memos, many=True)
        return Response(serializer.data)

    def post(self,request):
        request_memo = request.data.get("memo")
        user = request.user
        memo = NotePads.objects.filter(memo=request_memo , user = user)
        if not memo:
            serializer = NotePadSerializer(
                data=request.data, context={"user": user})
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        request_memo = request.GET.get("text",None)
        user = request.user
        memo = NotePads.objects.get(memo=request_memo , user=user)
        if memo is not None:
            memo.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        pass

