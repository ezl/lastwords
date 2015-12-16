from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

from phones.models import Phone

class Recipient(TimeStampedModel):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

class Notification(TimeStampedModel):
    recipient = models.ForeignKey(Recipient)
    phone = models.ForeignKey(Phone)

class NotificationSubscription(TimeStampedModel):
    phone = models.ForeignKey(Phone)
    recipient = models.ForeignKey(Recipient)

    active = models.BooleanField(
        verbose_name="Does the app user want to send notifications to this person?",
        default=True,
        )
    subscribed = models.BooleanField(
        verbose_name="Does the recipient want to receive these?",
        default=True,
        )

