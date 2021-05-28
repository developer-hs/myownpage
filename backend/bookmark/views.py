from decimal import Context
from functools import partial
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from bookmark.serializers import BookmarkSerializer
from notepad import serializers
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BookmarkAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        user = request.user
        bookmark = user.bookmark
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)


@api_view(["PUT"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def bookmark_site_locked(request):
    print(request.data)
    bookmark = request.user.bookmark
    serializer = BookmarkSerializer(bookmark ,data=request.data, partial=True)
    if serializer.is_valid():
        bookmark = serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


