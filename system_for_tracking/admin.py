from django.contrib import admin

from system_for_tracking.models import (
    Airport,
    AirplaneType,
    Airplane,
    Route,
    Crew,
    Flight,
    Order,
    Ticket
)


admin.site.register(Airport)
admin.site.register(AirplaneType)
admin.site.register(Airplane)
admin.site.register(Route)
admin.site.register(Crew)
admin.site.register(Flight)
admin.site.register(Order)
admin.site.register(Ticket)
