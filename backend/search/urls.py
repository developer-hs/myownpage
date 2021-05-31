from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("history/", views.SearchHistoryAPIView.as_view()),
    path("history/<int:pk>", views.SearchHistoryAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
