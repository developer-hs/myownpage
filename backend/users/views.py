
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes, authentication_classes
from rest_framework import serializers, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserInfoSerializer, UserSerializer
from .permission import IsSelf
from .models import User
from rest_framework.parsers import JSONParser

User = get_user_model()


@api_view(["POST"])
@permission_classes((AllowAny,))
@authentication_classes((JSONWebTokenAuthentication,))
def user_info(request):
    user = request.user
    serializer = UserInfoSerializer(user)
    return Response(serializer.data , status=status.HTTP_200_OK)