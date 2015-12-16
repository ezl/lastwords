from rest_framework import viewsets

from notifications.models import NotificationSubscription
from notifications.api.serializers import NotificationSubscriptionSerializer


class NotificationSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = NotificationSubscription.objects.all().order_by("-created")
    serializer_class = NotificationSubscriptionSerializer
