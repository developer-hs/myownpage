from django.urls.conf import path

from . import views


urlpatterns = [
    path("", views.ScheduleAPIView.as_view())
]
