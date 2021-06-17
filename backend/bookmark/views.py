from bookmark.models import BookmarkSites
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from bookmark import serializers
from bookmark.serializers import BookmarkSerializer, InputSite, InputSiteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AllSites(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, reuqest):
        sites = InputSite.objects.all()
        serializer = InputSiteSerializer(sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookmarkAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        user = request.user
        bookmark = user.bookmark
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)

    def put(self, request):
        setting_sites = request.data
        bookmark = request.user.bookmark
        for site_name in setting_sites:
            site = InputSite.objects.get(name=site_name)
            if setting_sites[site_name]:
                bookmark.sites.add(site)
            else:
                bookmark.sites.remove(site)
        return Response(status=status.HTTP_200_OK)


@api_view(["PUT"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def bookmark_site_locked(request):
    bookmark = request.user.bookmark
    serializer = BookmarkSerializer(bookmark, data=request.data, partial=True)
    if serializer.is_valid():
        bookmark = serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
