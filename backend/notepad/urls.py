from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("info", views.user_notepads_info),
    path("memo", views.create_memo),
    path("memo/delete",views.remove_memo)
]

urlpatterns = format_suffix_patterns(urlpatterns)
