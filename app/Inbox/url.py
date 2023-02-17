from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("inbox", views.InboxViewSet, basename="inbox")
router.register("inbox/users", views.InboxUserViewSet, basename="inbox_users")

urlpatterns = [path("", include(router.urls))]
