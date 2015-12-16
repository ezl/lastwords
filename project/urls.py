from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from phones.api.views import (
    PhoneViewSet,
    BatteryStatusViewSet,
    )
from notifications.api.views import NotificationSubscriptionViewSet


router = routers.DefaultRouter()
router.register('phone', PhoneViewSet)
router.register('battery_status', BatteryStatusViewSet)
router.register('notification_subscription', NotificationSubscriptionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
