
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet
)

app_name = "users"
router = DefaultRouter(trailing_slash=False)
router.register('', UserViewSet)

urlpatterns = router.urls
