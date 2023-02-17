from rest_framework import serializers
from .models import *


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = "__all__"


class InboxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxUser
        fields = "__all__"
