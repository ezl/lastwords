from rest_framework import serializers

from notifications.models import NotificationSubscription


class NotificationSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationSubscription
        fields = (
            'phone',
            'recipient',
            'active',
            'subscribed',
            )

