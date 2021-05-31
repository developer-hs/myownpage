from decimal import ConversionSyntax
from search.serializers import SearchHistorySerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import SearchHistory


class SearchHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        search_history = SearchHistory.objects.filter(user=request.user)
        serializer = SearchHistorySerializer(search_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SearchHistorySerializer(data=request.data)
        if serializer.is_valid():
            search_history = serializer.save(user=request.user)
            search_history_serializer = SearchHistorySerializer(
                search_history).data
            return Response(search_history_serializer, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        history = SearchHistory.objects.get(pk=pk, user=request.user)
        if history is not None:
            history.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
