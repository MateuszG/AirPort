from django.views import generic

from table.models import (
    Carrier,
    Flight
)


class IndexFlights(generic.ListView):
    template_name = 'table/home.html'
    context_object_name = 'flights'

    def get_queryset(self):
        return Flight.objects.filter()
