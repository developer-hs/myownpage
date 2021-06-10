from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("memo", views.NotepadsAPIView.as_view()),
    path("memo/<int:pk>/", views.NotepadsAPIView.as_view()),
    path("memo/<int:pk>/status", views.memo_status_toggle)
]

# urlpatterns = format_suffix_patterns(urlpatterns)
