import string
from datetime import timedelta

from django.db.models import (
    Model,
    DateTimeField,
    CharField,
    ForeignKey,
    IntegerField,
    TextField,
    URLField,
    PositiveIntegerField,
    DateField,
    NullBooleanField
)
from django.utils import timezone


class Flight(Model):
    flight_number = PositiveIntegerField(max_length=20, blank=True, null=True)
    airport_end = CharField(max_length=100, blank=True, null=True)
    departure = DateTimeField(
        blank=False, null=False, default=timezone.now
    )
    arrival = DateTimeField(
        blank=False, null=False, default=timezone.now
    )



class Carrier(Model):
    full_name = CharField(max_length=100, blank=True, null=True)
    flight = ForeignKey('Flight')

    def __str__(self):
        return self.full_name
