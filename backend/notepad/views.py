from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import NotePads
from .serializers import NotePadSerializer
from rest_framework.pagination import PageNumberPagination
from users.permission import IsSelf
import math


class OwnPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        done_count = len(NotePads.objects.filter(user = self.request.user).filter(done=True))
        print(done_count)
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page_size': math.ceil(self.page.paginator.count / self.page_size),
            'count': self.page.paginator.count,
            'done_count' : done_count,
            'results': data
        })


class NotepadsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        paginator = OwnPagination()
        notepads = NotePads.objects.all()
        result = paginator.paginate_queryset(notepads, request)
        serializer = NotePadSerializer(result, many=True, context={
                                       "request": request}).data
        return paginator.get_paginated_response(serializer)

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

    def put(self, request, pk):
        memo = NotePads.objects.get(pk=pk)
        if memo is not None:
            if memo.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = NotePadSerializer(
                memo, data=request.data, partial=True)
            if serializer.is_valid():
                memo = serializer.save()
                serializer_memo = NotePadSerializer(memo).data
                return Response(serializer_memo, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
