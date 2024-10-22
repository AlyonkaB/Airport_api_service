from django.db import IntegrityError

from rest_framework.validators import UniqueTogetherValidator

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


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("id", "name", "closest_big_city")


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "airplane_type")


class AirplaneListSerializer(AirplaneSerializer):
    airplane_type = serializers.StringRelatedField(many=False)

    class Meta:
        model = Airplane
        fields = ("id", "name", "airplane_type")


class AirplaneDetailSerializer(AirplaneSerializer):
    airplane_type = serializers.StringRelatedField(many=False)
    total_seats = serializers.SerializerMethodField()
    class Meta:
        model = Airplane
        fields = ("id", "name", "airplane_type", "rows", "seats_in_row", "total_seats")

    def get_total_seats(self, obj):
        return obj.rows * obj.seats_in_row


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ("id", "source", "destination", "distance")

    def validate(self, data):
        if data['source'] == data['destination']:
            raise serializers.ValidationError("Source and destination airports cannot be the same.")
        return data


class RouteListDetailSerializer(RouteSerializer):
    source = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name")


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ("id", "route", "airplane", "crew", "departure_time", "arrival_time")


class FlightListSerializer(serializers.ModelSerializer):
    route = serializers.StringRelatedField()
    class Meta:
        model = Flight
        fields = ("id", "route", "departure_time", "arrival_time")


class FlightDetailSerializer(FlightSerializer):
    route = serializers.StringRelatedField()
    airplane = serializers.StringRelatedField()
    crew = serializers.StringRelatedField(many=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "flight", "order")

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ticket with this row, seat, and flight already exists.")

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Ticket with this row, seat, and flight already exists.")
