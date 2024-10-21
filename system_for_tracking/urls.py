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
router.register("crew", CrewViewSet)
router.register("flight", FlightViewSet)
router.register("order", OrderViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "system_for_tracking"
