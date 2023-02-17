from django.shortcuts import render
import requests

# Create your views here.
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import *


class InboxViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = InboxSerializer
    queryset = Inbox.objects.all()


class InboxUserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = InboxSerializer
    queryset = Inbox.objects.all()
