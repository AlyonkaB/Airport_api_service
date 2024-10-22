from rest_framework import viewsets
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
from system_for_tracking.serializers import (
    AirportSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    RouteSerializer,
    CrewSerializer,
    FlightSerializer,
    OrderSerializer,
    TicketSerializer, AirplaneListSerializer, RouteListDetailSerializer, AirplaneDetailSerializer, FlightListSerializer,
    FlightDetailSerializer
)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == "list":
            return AirplaneListSerializer
        if self.action == "retrieve":
            return AirplaneDetailSerializer
        return serializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == "list" or self.action == "retrieve":
            return RouteListDetailSerializer
        return serializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == "list":
            return FlightListSerializer
        if self.action == "retrieve":
            return FlightDetailSerializer
        return serializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
