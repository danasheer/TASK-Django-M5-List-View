
from flights.models import Flight, Booking
from rest_framework import serializers


class ShowFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['destination', 'time', 'price', 'miles']


class UpcomingBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id']
