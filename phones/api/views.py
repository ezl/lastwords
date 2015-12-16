from rest_framework import viewsets

from phones.models import Phone, BatteryStatus
from phones.api.serializers import (
    PhoneSerializer,
    BatteryStatusSerializer,
    )


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all().order_by("-created")
    serializer_class = PhoneSerializer

class BatteryStatusViewSet(viewsets.ModelViewSet):
    queryset = BatteryStatus.objects.all().order_by("-created")
    serializer_class = BatteryStatusSerializer

