from django.contrib.admin import ModelAdmin, site, TabularInline

from .models import Flight, Carrier


class CarrierInline(TabularInline):
    model = Carrier
    extra = 1


class FlightAdmin(ModelAdmin):
    inlines = [CarrierInline]

site.register(Flight, FlightAdmin)
