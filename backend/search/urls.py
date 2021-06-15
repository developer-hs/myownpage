from search.models import SearchHistory
from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("history/", views.SearchHistoryAPIView.as_view()),
    path("history/<int:pk>", views.SearchHistoryAPIView.as_view()),
    path("history/all/<int:pk>",views.history_all_delete)
]

urlpatterns = format_suffix_patterns(urlpatterns)
