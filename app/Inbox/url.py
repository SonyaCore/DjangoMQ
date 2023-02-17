from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Views
from . import views
from Sender.views import SenderViewset

router = DefaultRouter()
router.register("inbox", views.InboxViewSet, basename="Inbox")
router.register("send", SenderViewset, basename="Send")
router.register("users", views.InboxUserViewSet, basename="inbox_users")

urlpatterns = [path("", include(router.urls))]
