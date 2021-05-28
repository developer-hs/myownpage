from sites.serializers import BookmarkSerializer
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
        bookmark = user.Bookmark.objects.all()
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)
