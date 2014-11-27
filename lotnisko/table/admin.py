from django.contrib.admin import ModelAdmin, site, TabularInline

from .models import Flight, Carrier


class FlightInline(TabularInline):
    model = Flight
    extra = 1


class CarrierAdmin(ModelAdmin):
    inlines = [FlightInline]

site.register(Carrier, CarrierAdmin)
