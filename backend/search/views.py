from rest_framework.decorators import api_view,  permission_classes, authentication_classes
from search.serializers import SearchHistorySerializer
from rest_framework import status, generics, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import SearchHistory
from users.permission import IsSelf


class SearchHistoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        historys = request.user.search_history.all()
        if historys:
            if historys.first().search_term == request.data.get("search_term"):
                return Response(status=status.HTTP_200_OK)
        if len(historys) == 8:
            historys.last().delete()
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


@api_view(["delete"])
@permission_classes((IsAuthenticated, IsSelf))
@authentication_classes((JSONWebTokenAuthentication,))
def history_all_delete(request, pk):
    if request.user.pk == pk:
        SearchHistory.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
