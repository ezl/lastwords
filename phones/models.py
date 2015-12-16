from __future__ import unicode_literals

from django.db import models

from django_extensions.db.models import TimeStampedModel


class Phone(TimeStampedModel):
    monitoring_active = models.BooleanField()
    human_name = models.CharField(
        verbose_name="The name of the human that belongs to this phone",
        max_length=50,
        )
    # number = Don't need
    # id = don't need probably need for subscriptions

    def get_battery_status(self):
        raise NotImplementedError
        # check phone
        battery_status = BatteryStatus.objects.create(
        )
        return battery_status

    def is_dying(self):
        raise NotImplementedError

    def might_be_dead(self):
        raise NotImplementedError


    def notify_subscribers(self):
        for subscription in self.notification_subscription.objects.filter(
                active=True,
                subscribed=True):
            to_phone_number = subscription.recipient.phone_number
            message = "Oh no! {}'s phone is dying!".format(self.human_name)
            # send_sms(to_phone_number, message)



class BatteryStatus(TimeStampedModel):
    UNKNOWN = "Unknown"
    UNPLUGGED = "Unplugged"
    CHARGING = "Charging"
    FULL = "Full"
    BATTERY_STATE_CHOICES = (
        ("?", UNKNOWN),
        ("U", UNPLUGGED),
        ("C", CHARGING),
        ("F", FULL),
        )

    phone = models.ForeignKey(Phone)
    level = models.FloatField()
    state = models.CharField(
        max_length=1,
        choices=BATTERY_STATE_CHOICES,
        default=UNKNOWN
        )



