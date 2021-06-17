
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from .models import NotePads
from .serializers import NotePadSerializer
from rest_framework.pagination import PageNumberPagination
import math


class OwnPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        done_count = len(NotePads.objects.filter(
            user=self.request.user).filter(done=True))

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page_size': math.ceil(self.page.paginator.count / self.page_size),
            'count': self.page.paginator.count,
            'done_count': done_count,
            'results': data
        })


class NotepadsAPIView(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = NotePads.objects.all()
    serializer_class = NotePadSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        paginator = OwnPagination()
        notepads = NotePads.objects.filter(user = request.user)
        result = paginator.paginate_queryset(notepads, request)
        serializer = NotePadSerializer(result, many=True, context={
                                       "request": request}).data
        return paginator.get_paginated_response(serializer)

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
