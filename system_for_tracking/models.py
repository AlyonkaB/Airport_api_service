from django.conf import settings
from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=255, unique=True)
    closest_big_city = models.CharField(max_length=255)

    def __str__(self):
        return f"Airport {self.name}({self.closest_big_city})"


class AirplaneType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField(null=False)
    seats_in_row = models.IntegerField(null=False)
    airplane_type = models.ForeignKey(AirplaneType, on_delete=models.CASCADE, related_name="airlines")

    def __str__(self):
        return f"{self.name} {self.airplane_type}"


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="routes_source")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="routes_destination")
    distance = models.IntegerField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['source', 'destination'], name='unique_route')
        ]

    def __str__(self):
        return f"{self.source} - {self.destination}"


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")
    crew = models.ManyToManyField(Crew, related_name="flights")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    @property
    def flight_duration(self):
        return self.departure_time - self.arrival_time

    def __str__(self):
        return f"{str(self.route)} {self.flight_duration}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.created_at)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['row', 'seat', 'flight'], name='unique_ticket')
        ]

    def __str__(self):
        return f"{str(self.flight)} (seat: {self.seat}, row: {self.row})"
