from django.urls.conf import path

from . import views


urlpatterns = [
    path("", views.ScheduleAPIView.as_view()),
    path("<int:pk>/", views.ScheduleAPIView.as_view())
]
