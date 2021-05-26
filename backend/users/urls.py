
from django.urls.conf import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("user_info", views.user_info),
    path("sign-up" , views.signup)
]

urlpatterns = format_suffix_patterns(urlpatterns)
