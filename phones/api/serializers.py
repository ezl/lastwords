from phones.models import Phone, BatteryStatus
from rest_framework import serializers


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = (
            'monitoring_active',
            'human_name',
            )

class BatteryStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BatteryStatus
        fields = (
            'phone',
            'level',
            'state',
            )
