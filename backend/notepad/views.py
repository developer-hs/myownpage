from decimal import ConversionSyntax
from django.contrib.auth import authenticate
from django.core.exceptions import RequestDataTooBig
from rest_framework import serializers, status
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

    def get(self, request):
        memos = NotePads.objects.filter(user=request.user)
        serializer = NotePadSerializer(memos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotePadSerializer(data=request.data)
        if serializer.is_valid():
            new_memo = serializer.save(user=request.user)
            new_memo_serializer = NotePadSerializer(new_memo).data
            return Response(new_memo_serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        memo = NotePads.objects.get(pk=pk)
        if memo is not None:
            if memo.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            memo.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request ,pk):
        memo = NotePads.objects.get(pk=pk)
        if memo is not None:
            if memo.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = NotePadSerializer(memo, data=request.data)
            if serializer.is_valid():
                memo = serializer.save()
                serializer_memo = NotePadSerializer(memo).data
                return Response(serializer_memo , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)



