from django.urls.conf import path
from . import views


urlpatterns = [
    path("memo", views.NotepadsAPIView.as_view()),
    path("memo/<int:pk>/", views.NotepadsAPIView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
