from django.urls import path, include
from rest_framework import routers

from system_for_tracking.views import (
    AirportViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    RouteViewSet,
    TicketViewSet,
    CrewViewSet,
    FlightViewSet,
    OrderViewSet
)

router = routers.DefaultRouter()
router.register("airport", AirportViewSet)
router.register("airplane-type", AirplaneTypeViewSet)
router.register("airplane", AirplaneViewSet)
router.register("route", RouteViewSet)
router.register("Crew", CrewViewSet)
router.register("Flight", FlightViewSet)
router.register("Order", OrderViewSet)
router.register("Ticket", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "system_for_tracking"
