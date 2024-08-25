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
from rest_framework import serializers


class AirportSerializer(serializers.Serializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirplaneTypeSerializer(serializers.Serializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneSerializer(serializers.Serializer):
    class Meta:
        model = Airplane
        fields = ("id", "name", "row", "seat_in_row", "airplane_type")


class RouteSerializer(serializers.Serializer):
    model = Route
    fields = ("id", "source", "destination", "distance")


class CrewSerializer(serializers.Serializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name")


class FlightSerializer(serializers.Serializer):
    class Meta:
        model = Flight
        fields = ("id", "route", "airplane", "crew", "departure_time", "arrival_time")


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "flight", "order")
